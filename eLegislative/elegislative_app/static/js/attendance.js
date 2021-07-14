$(document).ready(function () { 
    let tbl_attendance =  $('#tbl_attendance').DataTable({
        'columnDefs': [ {
            'targets': 7, /* column index */
            'orderable': false, /* true or false */
        }]
    }); 

    $("#tbl_attendance").on("click", ".btn-delete", function(e){
        e.preventDefault();
        let url = $(this).attr("data-url"); 
        let row = $(this).closest('tr');    
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
                $("#modal-default").data('tr',row).modal("show");
            },
            success: (data) =>{
                console.log(data.html_form)
                $("#modal-default .modal-content").html(data.html_form);
            },
            complete: (data) => {

            },
            error: (data) => {

            }

        });
        
        return false;
    });

    $("#modal-default").on("submit",".delete-attendance", function(e){
        e.preventDefault();
        let form = $(this);
        let row = $("#modal-default").data("tr");
        $.ajax({
            url: form.attr("data-url"),
            data: form.serialize(),
            cache: false,
            type: form.attr("method"),
            dataType: 'json',
            success: (data) => {
                if(data.form_is_valid){
                    $("#modal-default").modal("hide");
                    tbl_attendance.row(row).remove().draw();
                }else{
                    $("#modal-form .modal-content").html(data.html_form);
                }
            }
        });

        return false;

    });

});