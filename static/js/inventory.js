/**
 * Created by jlzhu on 16/5/9.
 */
$(document).ready(function() {
    document.session = $('#session').val();

    setTimeout(requestInventory, 100);

    $('#add-button').click(function(event) {
        $.ajax({
            url: 'http://127.0.0.1:8000/cart',
            type: 'POST',
            data: {
                session: document.session,
                action: 'add'
            },
            dataType: 'json',
            beforeSend: function(xhr, settings) {
                $(event.target).attr('disabled', 'disabled');
            },
            success: function(data, status, xhr) {
                console.log('Add success');
                $('#add-to-cart').hide();
                $('#remove-from-cart').show();
                $(event.target).removeAttr('disabled');
            }
        });
    });
    $('#remove-button').click(function(event) {
        $.ajax({
            url: 'http://127.0.0.1:8000/cart',
            type: 'POST',
            data: {
                session: document.session,
                action: 'remove'
            },
            dataType: 'json',
            beforeSend: function(xhr, settings) {
                $(event.target).attr('disabled', 'disabled');
            },
            success: function(data, status, xhr) {
                $('#remove-from-cart').hide();
                $('#add-to-cart').show();
                $(event.target).removeAttr('disabled');
            }
        });
    });
});

function requestInventory() {
    var host = 'ws://127.0.0.1:8000/cart/status';
    var websocket = new WebSocket(host);
    websocket.onopen = function(event) {};
    websocket.onmessage = function(event) {
        var data = $.parseJSON(event.data);
        $('#count').html(data['inventoryCount']);
    };
    websocket.onerror = function(event) {};
}