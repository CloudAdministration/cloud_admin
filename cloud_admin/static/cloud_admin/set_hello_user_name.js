$(document).ready(function () {
    const welcome_message = $('#welcome_message');
    $('#submit_user_name').click(function () {

        let user_name = $('#user_name').val();
        let welcome_user_message = welcome_message.text() + ' ' + user_name;
        if (welcome_user_message !== '')
            $('#welcome_message').text(welcome_user_message);

    })
});