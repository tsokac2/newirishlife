$('#new-image_1').change(function() {
    var file = $('#new-image_1')[0].files[0];
    $('#filename_1').text(`Image file:${file.name}`);
});
$('#new-image_2').change(function() {
    var file = $('#new-image_2')[0].files[0];
    $('#filename_2').text(`Image file: ${file.name}`);
});
$('#new-image_3').change(function() {
    var file = $('#new-image_3')[0].files[0];
    $('#filename_3').text(`Image file: ${file.name}`);
});