#!/usr/bin/perl

use CGI;

# Create a CGI.pm object
my $cgi = new CGI;

# Get the form data
my $email_address = $cgi->param('email_address');
my $feedback = $cgi->param('feedback');
my $contact_name =  $cgi->param('contact_name');

# Filter the form data
$email_address = filter_email_header($email_address);
$feedback = filter_form_data($feedback);

# Email the form data
open ( MAIL, "| /usr/lib/sendmail -t" );
print MAIL "From: $email_address\n";
print MAIL "To: attl\@rita.com\n";
print MAIL "Subject: Feedback Form Submission\n\n";
print MAIL "Name - $contact_name\n\n";
print MAIL "$feedback\n $name\n";
print MAIL "\n.\n";
close ( MAIL );

# Print the HTTP header
print $cgi->header(-type => 'text/html');

# Print the HTML thank you page
print <<HTML_PAGE;
<html>
<head>
<title>Thank You</title>
</head>
<body>
<h1>Thank You</h1>
<p>Thank you for your feedback.</p>
</body>
</html>
HTML_PAGE

# Functions to filter the form data

sub filter_email_header
{
my $form_field = shift;
$form_field = filter_form_data($form_field);
$form_field =~ s/[\0\n\r\|\!\/\<\>\^\$\%\*\&]+/ /g;

return $form_field ;
}

sub filter_form_data
{
my $form_field = shift;
$form_field =~ s/From://gi;
$form_field =~ s/To://gi;
$form_field =~ s/BCC://gi;
$form_field =~ s/CC://gi;
$form_field =~ s/Subject://gi;
$form_field =~ s/Content-Type://gi;

return $form_field ;
}
