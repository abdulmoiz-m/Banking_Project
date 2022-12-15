let i=1;
while(true) {
    if ($('#amount_'+i).length) {
        let balance = parseInt($('#balance').text());
        let sign = $('#amount_'+i).text().substring(0,1);
        let change = parseInt($('#amount_'+i).text().substring(2));

        if (sign === '-') {
            balance -= change
        } else if (sign === '+') {
            balance += change
        }
        $('#rem_Bal_'+i).text('$' + (balance));
        $('#balance').text(balance)
        i++;
    }
    else {
        break;
    }
}