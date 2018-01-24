ko.validation.init({
    registerExtenders: true,
    messagesOnModified: true,
    insertMessages: true,
    parseInputAttributes: true,
    errorClass: 'errorStyle',
    messageTemplate: null
}, true);

function SignUpViewModel()
{
    
    var self = this;
    self.validateNow = ko.observable(false);
    self.username = ko.observable().extend({
        required: true,
        minLength: 3
    });
    self.password = ko.observable().extend({ required: true, minLength: 3 });
	self.login_error = ko.observable("tyu")
    self.errors = ko.validation.group(self);
	
    self.signup = function () {
        self.validateNow(true);
		validdata = {username:self.username, password:self.password}
        if (self.errors().length === 0) {
            $.ajax({
                url: 'api-token-auth',
                type: 'POST',
                data: validdata,
                success: function (data) {
					window.sessionStorage.accessToken = data.token;
                    window.location.href = "/featurescreen";
                },
				error: function(data){
					$('#errorspan').text(JSON.parse(data.responseText).non_field_errors)
				}
            });
        }
        else {
            self.errors.showAllMessages();
            return;
        }
       
    }
    
}
ko.applyBindings(new SignUpViewModel());
