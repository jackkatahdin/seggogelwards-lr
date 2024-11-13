var button_r = $("#forward_button");
button_r.click(function() {
    console.log(button_r.text());
    if (button_r.text() === "Forward") {
        $.ajax({
            url: "/forward_turn",
            type: "post",
            success: function(response) {
                console.log(response);
                button_r.text("Stop");
            }
        });
    } else {
        $.ajax({
            url: "stop",
            type: "post",
            success: function() {
                button_r.text("Forward");
            }
        })
    }
});
var button_y = $("#backward_button");
button_y.click(function() {
    console.log(button_y.text());
    if (button_y.text() === "Backward") {
        $.ajax({
            url: "/backward_turn",
            type: "post",
            success: function(response) {
                console.log(response);
                button_y.text("Stop");
            }
        });
    } else {
        $.ajax({
            url: "/stop",
            type: "post",
            success: function() {
                button_y.text("Backward");
            }
        })
    }
});
