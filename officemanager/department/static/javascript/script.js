function rm_tr(element){
    if(window.confirm("Do you really want to delete this record?")){
        element.closest('table').deleteRow(element.closest('tr').rowIndex);
    }
    else{
        return 0;
    }
}
