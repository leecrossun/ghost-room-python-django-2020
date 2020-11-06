// setInterval("refresh()", 1000);

function refresh() {
    $.ajax({
      type: "POST",
      url: "{% url 'chat_refresh' my_room.id %}",
      data: {
        'pk': $(this).attr('name'),
        'csrfmiddlewaretoken': '{{ csrf_token }}'
      },
      dataType: "json",
      success: function (response) {
        //document.getElementById('here').innerHTML = "성공<br>";
        var chat = "";
        for (i in response) {
          var message = JSON.parse(response[i])
          var sameuser = false;
          for (var key in message) {
            if (key == "sender") {
              if (message[key] == "{{user.username}}") {
                sameuser = true;
                chat += '<div class="message-right">';
                chat += '<div class="sender sender-right">';
                chat += message[key];
                chat += '</div>';
              } else {
                chat += '<div class="message-left">';
                chat += '<div class="sender sender-left">';
                chat += message[key];
                chat += '</div>';
              }
            } else if (key == "body") {
              if (sameuser) {
                sameuser = false;
                chat += '<div class="body body-right">';
                chat += message[key];
                chat += '</div>';
                chat += '</div>';
              } else {
                chat += '<div class="body body-left">';
                chat += message[key];
                chat += '</div>';
                chat += '</div>';
              }
            }
          }
        }
        document.getElementById('chat').innerHTML = chat;
      }
    });
  }