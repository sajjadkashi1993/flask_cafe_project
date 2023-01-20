
window.addEventListener('load', (event) => {
    updateUserCart();
    const elems = document.getElementsByClassName('showing-category');
    elems[0].style.display='block';
});


// The function for send new cart data to url
function sendCartData(id, quantity) {
    const listData = [
        {"id": id,
        "quantity": quantity}
    ];
    $.ajax({
        type: "POST",
        url: "/update-cart-data",
        data: JSON.stringify(listData),
        contentType: "application/json",
        dataType: 'json',
        success: function(result) {
            console.log("POST Result:");
            console.log(result);
        } 
    });
}

// The function for update cart data for shop page
function updateUserCart() {
    $.ajax({
        type: "GET",
        url: "/update-cart-data",
        success: function(result) {
            const item_quantity = JSON.parse(result);
            Object.entries(item_quantity).map(item => {
                showHideCartButton(item[1]['id'], item[1]['quantity'])
              })
        }
    });
};

// The function for Add item to cart with number of 1
function showHideCartButton(item_id, value) {
    document.getElementById('add_to_cart_'+item_id).style.display = "none";
    document.getElementById('manipulate_quantity_'+item_id).style.display = "block";
    document.getElementById('input-'+item_id).value = value;
    // send data to url
    sendCartData(item_id, 1);
}

// The function for manipulating quanitities of each item:
jQuery(document).ready(function(){
    // This button will increment the value
    $('[data-quantity="plus"]').click(function(e){
        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        fieldName = $(this).attr('data-field');
        // Get its current value
        var currentVal = parseInt($('input[name='+fieldName+']').val());
        $('input[name='+fieldName+']').val(currentVal + 1);
        // send data to url
        sendCartData(fieldName, (currentVal + 1));
    });
    // This button will decrement the value till 0
    $('[data-quantity="minus"]').click(function(e) {
        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        fieldName = $(this).attr('data-field');
        // Get its current value
        var currentVal = parseInt($('input[name='+fieldName+']').val());
        // If it is greater than 0
        if (currentVal > 1) {
            // Decrement one
            $('input[name='+fieldName+']').val(currentVal - 1);
            // send data to url
            sendCartData(fieldName, (currentVal - 1));
        } else {
            // Otherwise put a 0 there and change the manipulation div to add_to_cart
            $("#manipulate_quantity_"+fieldName).hide();
            $("#add_to_cart_"+fieldName).show();
            $('input[name='+fieldName+']').val(0);
            // send data to url
            sendCartData(fieldName, 0);
        }
    });
});

// A function for show/hide categories when User click on them
function showCategories(name){

    let elems = document.getElementsByClassName('showing-category');
    for (var i=0;i<elems.length;i+=1){
        elems[i].style.display='none';
    };
    document.getElementById(name+'-menu').style.display='block';
}


function orderStateOption(num){
    if (num ==='1'){
        document.getElementById('table-box').style.display = 'block'
        document.getElementById("address-box").style.display = 'none'
    }else if (num==='2'){
       document.getElementById('table-box').style.display = 'none'
        document.getElementById("address-box").style.display = 'block'
    }else {
        document.getElementById('table-box').style.display = 'none'
        document.getElementById("address-box").style.display = 'none'
    }
}