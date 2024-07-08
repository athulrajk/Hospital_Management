
function patientValidation() {
    let error = false;
    const validationMessages = $('#validation-messages');
    validationMessages.hide();

    const fields = [
        { id: 'registrationId', message: 'Please Enter Registration Id' },
        { id: 'title', message: 'Please Enter Title' },
        { id: 'firstName', message: 'Please Enter First Name' },
        { id: 'lastName', message: 'Please Enter Last Name' },
        { id: 'recNo', message: 'Please Enter Rec No' },
        { id: 'address', message: 'Please Enter Address' },
        { id: 'locality', message: 'Please Enter Locality' },
        { id: 'city', message: 'Please Enter City' },
        { id: 'State', message: 'Please Enter State' },
        { id: 'age', message: 'Please Enter Age' },
        { id: 'mobile', message: 'Please Enter Mobile' },
        { id: 'dob', message: 'Please Enter DOB' },
        { id: 'gender', message: 'Please Enter Gender' },
        { id: 'guardianName', message: 'Please Enter Guardian Name' },
        { id: 'opNumber', message: 'Please Enter Op Number' },
        { id: 'passportNumber', message: 'Please Enter Passport Number' },
        { id: 'dischargeDate', message: 'Please Enter Discharage Date' },
        { id: 'country', message: 'Please Enter Country' },
        { id: 'zip', message: 'Please Enter Zip' },
        { id: 'phonenumber', message: 'Please Enter Phone Number' },
        { id: 'Medicalhistory', message: 'Please Enter Medical History' },
        { id: 'bloodgroup', message: 'Please Enter Blood group' },
        { id: 'payment', message: 'Please Enter Payment' },
        { id: 'conditions', message: 'Please Enter Condition' },
        { id: 'pregnant', message: 'Please Enter Pregnant' },
        { id: 'referredBy', message: 'Please Enter Referred By' },
        { id: 'occupation', message: 'Please Enter Occupation' },
        { id: 'photo', message: 'Please add Photo' },
        { id: 'specialization', message: 'Please Enter Specialization' },
        { id: 'doctor', message: 'Please Enter Doctor' },
        { id: 'referredBy', message: 'Please Enter Referred By' },
    ];

    for (let field of fields) {
        if ($(`#${field.id}`).val() === '') {
            validationMessages.show().html(field.message);
            error = true;
            break;
        }
    }

    return !error;
}

document.getElementById('photo').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.getElementById('selectedPhoto');
            img.src = e.target.result;
            img.style.display = 'block';
        }
        reader.readAsDataURL(file);
    }
});


$('#patientform').submit(function(event) {
    event.preventDefault();
    var formData = new FormData($(this)[0]); // Create FormData object with form data
    var fileInput = $('#photo')[0].files[0]; // Get the file input
    formData.append('photo', fileInput);
    console.log("formccData",formData)
    if (patientValidation()) {
    $.ajax({
        url: '/submit_patient',
        type: 'POST',
        data: formData,
        contentType: false, // Prevent jQuery from setting contentType
        processData: false,
        success: function(response) {
        window.location.href = '/patientdashboard';
        }
    });
}
});




//   $('#patientform').submit(function(event) {
//         event.preventDefault();
//         var form = $(this);
//         console.log("fdddorm",form)

//         if (patientValidation()) {
//         var formData = new FormData($(this)[0]); // Create FormData object with form data
//         var fileInput = $('#photo')[0].files[0]; // Get the file input
//         formData.append('photo', fileInput);

//           $.ajax({
//               url: '/submit_patient',
//               type: 'POST',
//               data: formData,
//               contentType: false, // Prevent jQuery from setting contentType
//               processData: false,
//               success: function(response) {
//                 window.location.href = '/patientdashboard';
//               }
//           });
//         }
//     });