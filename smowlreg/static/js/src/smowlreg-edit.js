function SmowlRegXBlock(runtime, element) {
    $('.cancel-button', element).bind('click', function() {
        runtime.notify('cancel', {});
    });
}
