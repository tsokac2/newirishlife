var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var cardNumber = elements.create('cardNumber',  {
    showIcon: true,
    classes : {
        base : "StripeElement",
        focus : "StripeElement--focus",
        invalid: "card-error"
    }
});
var cardExpiry = elements.create('cardExpiry', {
    classes : {
        invalid: "card-error"
    }
});
var cardCvc = elements.create('cardCvc');

cardNumber.mount('#card-number');
cardExpiry.mount('#exdate');
cardCvc.mount('#cvc');

cardNumber.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="card-icon-error" role="alert">
                <i class="fas fa-exclamation-triangle"></i>
            </span>
            <span class="card-number-error">${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

cardExpiry.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-expiry-errors');
    if (event.error) {
        var html = `
            <span class="card-icon-error" role="alert">
                <i class="fas fa-exclamation-triangle"></i>
            </span>
            <span class="card-number-error">${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    cardNumber.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#blur-overlay').fadeToggle(100);

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

 $.post(url, postData).done(function () {
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card : cardNumber,
            billing_details: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.city.value),
                    country: $.trim(form.country.value),
                    state: $.trim(form.county.value),
                }
            }
        },
        shipping: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            address: {
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address2.value),
                city: $.trim(form.city.value),
                country: $.trim(form.country.value),
                postal_code: $.trim(form.postcode.value),
                state: $.trim(form.county.value),
            }
        },
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="card-icon-error" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span class="card-number-error">${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#blur-overlay').fadeToggle(100);
                cardNumber.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        location.reload();
    });
});