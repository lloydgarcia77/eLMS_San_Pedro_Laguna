$(document).ready(function () {
    let table =  $('#table_audio_recording').DataTable({
        'columnDefs': [ {
            'targets': 7, /* column index */
            'orderable': false, /* true or false */
        }]
    }); 
});