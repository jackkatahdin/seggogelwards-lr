var button_f = $("#forward_button");
button_f.click(function() {
    console.log(button_f.text());
    if (button_f.text() === "Forward") {
        $.ajax({
            url: "/forward_turn",
            type: "post",
            success: function(response) {
                console.log(response);
                button_f.text("Stop");
            }
        });
    } else {
        $.ajax({
            url: "/stop",
            type: "post",
            success: function() {
                button_f.text("Forward");
            }
        })
    }
});
var button_b = $("#backward_button");
button_b.click(function() {
    console.log(button_b.text());
    if (button_b.text() === "Backward") {
        $.ajax({
            url: "/backward_turn",
            type: "post",
            success: function(response) {
                console.log(response);
                button_b.text("Stop");
            }
        });
    } else {
        $.ajax({
            url: "/stop",
            type: "post",
            success: function() {
                button_b.text("Backward");
            }
        })
    }
});
var button_r = $("#right_button");
button_r.click(function() {
    console.log(button_r.text());
    if (button_r.text() === "Right") {
        $.ajax({
            url: "/right_turn",
            type: "post",
            success: function(response) {
                console.log(response);
                button_r.text("Stop");
            }
        });
    } else {
        $.ajax({
            url: "/stop",
            type: "post",
            success: function() {
                button_r.text("Right");
            }
        })
    }
});
var button_l = $("#left_button");
button_l.click(function() {
    console.log(button_l.text());
    if (button_l.text() === "Left") {
        $.ajax({
            url: "/left_turn",
            type: "post",
            success: function(response) {
                console.log(response);
                button_l.text("Stop");
            }
        });
    } else {
        $.ajax({
            url: "/stop",
            type: "post",
            success: function() {
                button_l.text("Left");
            }
        })
    }
});
