function filter(){
    var input, input_1, input_2, tr, td, ateTd;

    input =[document.getElementById('birth-from').value, document.getElementById('birth-to').value];
    if(input[0] == ""){
        input[0] = new Date(0,0,0);
    }
    else{
        input[0] = new Date(input[0]);
    }
    if(input[1] == ""){
        input[1] = new Date(9999,12,32);
    }
    else{
        input[1] = new Date(input[1]);
    }
    input.forEach(element => {
        element.setHours(0,0,0,0);
    });

    if(input[0] > input[1]){
        alert('Incorrect date format');
        document.getElementById('birth-from').value = ""
        document.getElementById('birth-to').value = ""
        return 0;
    }

    tr = document.getElementById('table-employees').querySelectorAll('tbody > tr');
    
    for(i = 0; i < tr.length; i++){
        td = tr[i].getElementsByTagName('td')[3].textContent.split('.');
        dateTd = new Date(td[2], td[1]-1, td[0]);
        if (dateTd >= input[0] && dateTd <= input[1]){
            tr[i].style.display = '';}
        else{
            tr[i].style.display = 'none';
        }
    }
}

function rm_tr(element){
    if(window.confirm("Do you really want to delete this record?")){
        element.closest('table').deleteRow(element.closest('tr').rowIndex);
    }
    else{
        return 0;
    }
}