$(document).ready(function() {
    var max_fields      = 10;
    var wrapper   		= $(".input_fields_wrap");
    var add_button      = $(".add_field_button");

    var x = 1;
    $(add_button).click(function(e){
    e.preventDefault();
        if(x < max_fields){
            x++;
            $(wrapper).append('' +
                '<div class="input-group mb-3">' +
                '<input placeholder="Enter order number" type="text" name="order_1c" class="form-control">' +
                '<div class="input-group-append">' +
                '<button class="btn btn-outline-danger remove_field" type="button">Remove</button>' +
                '</div></div>');
        }
    });

    $(wrapper).on("click",".remove_field", function(e){
        e.preventDefault(); $(this).parent('div').parent('div').remove(); x--;
        })
});