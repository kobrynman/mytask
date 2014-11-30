    function updateData() {
        $.ajax({
            url: "/updatedata/",
            type: "post",
            success : function(response)
            {
                debugger;
                $("#example").find("tr:gt(0)").remove();
                for(var i = 0; i < response.length; i++) {
                    var html =
                        "<tr>" +
                            "<td><a href='/personlist/"+response[i].id+"'>"+response[i].name+"</a></td>" +
                            "<td><a href='/personlist/"+response[i].id+"'>"+response[i].last_name+"</a></td>" +
                            "<td><a href='/personlist/"+response[i].id+"'>"+response[i].phone+"</a></td>" +
                        "</tr>";
                    $('#example').append(html);
                }
            }
        });
    }

    function findByPhone() {
        var userPhone = $("#phone").val();
        if(userPhone != "") {
            $("#phone").css("border-color", "#cccccc");
            $.ajax({
                url: "/findbyphone/",
                data: {phone:userPhone},
                type: "post",
                success : function(response)
                {
                    debugger;
                    alert(response.name);
                }
            });
        }
        else {
            $("#phone").css("border-color", "red");
            $("#phone").focus();
        }
    }

    function resetBorder() {
        $("#phone").css("border-color", "#cccccc");
    }