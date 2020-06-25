from project.server.common.email.message import make_email, EmailMessage, make_html_mail, EmailMultiAlternatives


class TestEMail:

    def test_make_mail(self):
        msg = make_email(to_list="leon.morten@gmail.com", from_address="anfrage@smartphoniker.de",
                         subject="Ich will das hier html drinnen ist", body="Blaa")

        assert isinstance(msg, dict)
        mail = EmailMessage.from_dict(msg)
        assert isinstance(mail, EmailMessage)
        assert mail.to == ["leon.morten@gmail.com"]
        assert mail.from_email == "anfrage@smartphoniker.de"
        assert mail.subject == "Ich will das hier html drinnen ist"
        assert mail.body == "Blaa"
        assert mail.content_subtype == 'plain'

        payload = mail.message()
        assert payload.get_content_type() == "text/plain"
        assert payload.get_charset() == "utf-8"

    def test_html_mail(self):
        msg = make_html_mail(to_list="leon.morten@gmail.com", from_address="anfrage@smartphoniker.de",
                             subject="Ich will das hier html drinnen ist", html_body="<h1> HEADER </h1>")

        assert isinstance(msg, dict)
        mail = EmailMessage.from_dict(msg)
        assert isinstance(mail, EmailMessage)
        assert mail.to == ["leon.morten@gmail.com"]
        assert mail.from_email == "anfrage@smartphoniker.de"
        assert mail.subject == "Ich will das hier html drinnen ist"
        assert mail.body == "<h1> HEADER </h1>"
        assert mail.content_subtype == 'html'

        payload = mail.message()
        assert payload.get_content_type() == "text/html"
        assert payload.get_charset() == "utf-8"

    def test_html_mail_alternative(self):
        msg = make_html_mail(to_list="leon.morten@gmail.com", from_address="anfrage@smartphoniker.de",
                             subject="Ich will das hier html drinnen ist", html_body="<h1> HEADER </h1>")
        mail = EmailMultiAlternatives.from_dict(msg)
        assert isinstance(mail, EmailMultiAlternatives)

        mail.attach_alternative('A text Alternative', 'text/plain')
        assert mail.message()
