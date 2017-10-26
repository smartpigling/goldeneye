// App initialization code goes here

//Open active sidebar menu
$(".sidebar-menu li[class='active']").parents("li").addClass("active menu-open");


$("#demo").DataTable({
    "ajax": {
        "url": "/users/user_table/",
        "dataSrc": "data"
    },
    "columns": [
        {"data": "id"},
        {"data": "username"},
        {"data": "active"}
    ]
});