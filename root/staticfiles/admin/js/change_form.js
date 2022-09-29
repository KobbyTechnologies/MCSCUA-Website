<<<<<<< HEAD
/*global gettext*/
=======
>>>>>>> 89ce836f4d54b5e65ca84936565d5dc8994143e6
'use strict';
{
    const inputTags = ['BUTTON', 'INPUT', 'SELECT', 'TEXTAREA'];
    const modelName = document.getElementById('django-admin-form-add-constants').dataset.modelName;
<<<<<<< HEAD
    let submitted = false;

    if (modelName) {
        const form = document.getElementById(modelName + '_form');

        form.addEventListener('submit', (event) => {
            event.preventDefault();
            if (submitted) {
                const answer = window.confirm(gettext('You have already submitted this form. Are you sure you want to submit it again?'));
                if (!answer) {return;}
            };
            event.target.submit();
            submitted = true;
        });

=======
    if (modelName) {
        const form = document.getElementById(modelName + '_form');
>>>>>>> 89ce836f4d54b5e65ca84936565d5dc8994143e6
        for (const element of form.elements) {
            // HTMLElement.offsetParent returns null when the element is not
            // rendered.
            if (inputTags.includes(element.tagName) && !element.disabled && element.offsetParent) {
                element.focus();
                break;
            }
        }
    }
}
