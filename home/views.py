# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.core.mail import send_mail
# from django.conf import settings
# from django.shortcuts import render
# import traceback
# import threading
# from django.core.mail import EmailMessage, get_connection
# import time








# # Create your views here.

# def index(request):
#     return render(request, "index.html")

# def about(request):
#     return render(request, "about.html")

# def contact(request):
#     return render(request, "contact.html")

# def rides(request):
#     return render(request, "rides.html")

# def _send_mail_async(subject, message, from_email, recipient_list):
#     try:
#         send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#     except Exception as e:
#         # log error - don't crash request
#         print("Async EMAIL ERROR:", e)
#         traceback.print_exc()



# def news_and_events(request):
#     return render(request, "news_and_events.html")

# def careers(request):
#      return render(request, "careers.html")

# def little_peppe(request):
#     return render(request, "little_peppe.html")

# def peppe_toys(request):
#     return render(request, "peppe_toys.html")

# def packages(request):
#     return render(request, "packages.html")

# def locations(request):
#     return render(request, "locations.html")

# def enquiry(request):
#     return render(request, "enquiry.html")

# def base(request):
#     return render(request, "base.html")


# def testimonials(request):
#     return render(request, "testimonials.html")

# def homeheader(request):
#     return render(request, "homeheader.html")

# def homefooter(request):
#     return render(request, "homefooter.html")

# def peppe_party(request):
#     return render(request, "peppe_party.html")

# def peppe_cafe(request):
#     return render(request, "peppe_cafe.html")

# def terms_and_conditions(request):
#     return render(request, "terms_and_conditions.html")

# def faq(request):
#     return render(request, "faq.html")

# def privacy_and_policy(request):
#     return render(request, "privacy_and_policy.html")

# def activities(request):
#     return render(request, "activities.html")

# def offers(request):
#     return render(request, "offers.html")

# # def get_in_touch(request):
# #     if request.method == "POST":
    
# #         name = request.POST.get("name")
# #         email = request.POST.get("email")
# #         phone = request.POST.get("phone")
# #         subject = request.POST.get("subject")
# #         message_text = request.POST.get("message")

# #         email_subject = f"New contact message from {name}: {subject}"
# #         email_body = f"""
# # You received a new message from the website:

# # Name: {name}
# # Email: {email}
# # Phone: {phone}
# # Subject: {subject}

# # Message:
# # {message_text}
# # """

# #         try:
# #             send_mail(
# #                 email_subject,
# #                 email_body,
# #                 settings.DEFAULT_FROM_EMAIL,
# #                 ["online@funridersindia.com"],
# #                 fail_silently=False,
# #             )
# #             messages.success(request, "Your message has been sent successfully.")

# #         except Exception as e:
# #             print("EMAIL ERROR:", e)        
# #             traceback.print_exc()           
# #             messages.error(request, "Something went wrong while sending your message.")

# #         return redirect("get_in_touch")

# #     return render(request, "get_in_touch.html")

# # def _send_mail_async(subject, message, from_email, recipient_list):
# #     try:
# #         send_mail(subject, message, from_email, recipient_list, fail_silently=False)
# #     except Exception as e:
# #         # log error - don't crash request
# #         print("Async EMAIL ERROR:", e)
# #         traceback.print_exc()

# # def get_in_touch(request):
# #     if request.method == "POST":
# #         name = request.POST.get("name")
# #         email = request.POST.get("email")
# #         phone = request.POST.get("phone")
# #         subject = request.POST.get("subject")
# #         message_text = request.POST.get("message")

# #         email_subject = f"New contact message from {name}: {subject}"
# #         email_body = f"""
# # You received a new message from the website:

# # Name: {name}
# # Email: {email}
# # Phone: {phone}
# # Subject: {subject}

# # Message:
# # {message_text}
# # """

# #         try:
# #             # send admin email in background
# #             threading.Thread(
# #                 target=_send_mail_async,
# #                 args=(email_subject, email_body, settings.DEFAULT_FROM_EMAIL, ["online@funridersindia.com"]),
# #                 daemon=True,
# #             ).start()

# #             # send user auto-reply in background
# #             auto_reply_subject = "Thank You for Contacting Us!"
# #             auto_reply_message = f"Hi {name},\n\nThank you for reaching out to us. We have received your message and our team will get back to you soon.\n\nIf your enquiry is urgent, \n\nplease contact: +91 907220 05555\n\nRegards,\nPeppe Planet Team"
# #             threading.Thread(
# #                 target=_send_mail_async,
# #                 args=(auto_reply_subject, auto_reply_message, settings.DEFAULT_FROM_EMAIL, [email]),
# #                 daemon=True,
# #             ).start()

# #             messages.success(request, "Your message has been sent successfully. We will contact you soon.")
# #         except Exception:
# #             messages.error(request, "Something went wrong while sending your message.")

# #         return redirect("get_in_touch")

# #     return render(request, "get_in_touch.html")

# # def _send_two_emails_in_background(admin_subject, admin_body, admin_to,
# #                                    user_subject, user_body, user_to):

# #     try:
# #         t0 = time.time()

# #         conn = get_connection(
# #             host=settings.EMAIL_HOST,
# #             port=settings.EMAIL_PORT,
# #             username=settings.EMAIL_HOST_USER,
# #             password=settings.EMAIL_HOST_PASSWORD,
# #             use_tls=settings.EMAIL_USE_TLS,
# #             use_ssl=getattr(settings, "EMAIL_USE_SSL", False),
# #             timeout=getattr(settings, "EMAIL_TIMEOUT", None),
# #         )
# #         print("get_connection took", time.time() - t0, "seconds")

# #         t1 = time.time()
# #         # open connection explicitly (reduces hidden per-send overhead)
# #         conn.open()
# #         print("conn.open() took", time.time() - t1, "seconds")

# #         admin_msg = EmailMessage(..., connection=conn)
# #         user_msg = EmailMessage(..., connection=conn)

# #         t2 = time.time()
# #         conn.send_messages([admin_msg, user_msg])
# #         print("send_messages took", time.time() - t2, "seconds")

# #     except Exception as e:
# #         print("Async EMAIL ERROR:", e)
# #         traceback.print_exc()

# def peppe_style(request):
#     return render(request, "peppe_style.html")
 
# def activities_detail(request):
#     return render(request, "activities_detail.html")
 


# def _send_mail_async(subject, message, from_email, recipient_list):
#     try:
#         send_mail(
#             subject=subject,
#             message=message,
#             from_email=from_email,
#             recipient_list=recipient_list,
#             fail_silently=False,
#         )
#     except:
#         pass


# def franchise(request):

#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         subject = request.POST.get("subject")
#         message_text = request.POST.get("message")

#         email_subject = f"New contact message from {name}: {subject}"
#         email_body = f"""
# You received a new message from the website:

# Name: {name}
# Email: {email}
# Phone: {phone}
# Subject: {subject}

# Message:
# {message_text}
# """

#         try:
#             # admin mail
#             threading.Thread(
#                 target=_send_mail_async,
#                 args=(email_subject, email_body, settings.DEFAULT_FROM_EMAIL, ["online@funridersindia.com"]),
#                 daemon=True,
#             ).start()

#             # user auto reply
#             auto_reply_subject = "Thank You for Contacting Us!"
#             auto_reply_message = f"""Hi {name},

# Thank you for reaching out to us. We have received your message and our team will get back to you soon.

# If your enquiry is urgent, please contact: +91 907220 05555

# Regards,
# Peppe Planet Team
# """

#             threading.Thread(
#                 target=_send_mail_async,
#                 args=(auto_reply_subject, auto_reply_message, settings.DEFAULT_FROM_EMAIL, [email]),
#                 daemon=True,
#             ).start()

#             messages.success(request, "Your message has been sent successfully. We will contact you soon.")

#         except:
#             messages.error(request, "Something went wrong while sending your message.")

#         # ❗ IMPORTANT: Re-render same page, not redirect
#         return render(request, "franchise.html")

#     # GET → just show page
#     return render(request, "franchise.html")

# # views.py (replace your existing functions with this block)

# import threading
# import time
# import traceback
# import logging

# from django.conf import settings
# from django.core.mail import send_mail, get_connection, EmailMessage
# from django.http import JsonResponse
# from django.shortcuts import render, redirect
# from django.contrib import messages

# logger = logging.getLogger(__name__)


# def _send_mail_async(subject, message, from_email, recipient_list):
#     """Simple single-email wrapper (keeps your original helper)."""
#     try:
#         send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#     except Exception as e:
#         logger.exception("Async single send_mail failed: %s", e)


# def _send_two_emails_in_background(admin_subject, admin_body, admin_to,
#                                    user_subject, user_body, user_to):
#     """
#     Open one SMTP connection and send two EmailMessage objects (admin + user).
#     Designed to run in a background thread.
#     """
#     try:
#         t0 = time.time()
#         conn = get_connection(
#             host=getattr(settings, "EMAIL_HOST", None),
#             port=getattr(settings, "EMAIL_PORT", None),
#             username=getattr(settings, "EMAIL_HOST_USER", None),
#             password=getattr(settings, "EMAIL_HOST_PASSWORD", None),
#             use_tls=getattr(settings, "EMAIL_USE_TLS", False),
#             use_ssl=getattr(settings, "EMAIL_USE_SSL", False),
#             timeout=getattr(settings, "EMAIL_TIMEOUT", None),
#         )
#         logger.debug("get_connection took %.3fs", time.time() - t0)

#         t1 = time.time()
#         conn.open()
#         logger.debug("conn.open() took %.3fs", time.time() - t1)

#         from_email = getattr(settings, "DEFAULT_FROM_EMAIL", settings.EMAIL_HOST_USER)

#         admin_msg = EmailMessage(
#             subject=admin_subject,
#             body=admin_body,
#             from_email=from_email,
#             to=admin_to,
#             connection=conn,
#         )

#         user_msg = EmailMessage(
#             subject=user_subject,
#             body=user_body,
#             from_email=from_email,
#             to=user_to,
#             connection=conn,
#         )

#         t2 = time.time()
#         sent = conn.send_messages([admin_msg, user_msg])  # returns number of messages sent (or None)
#         logger.debug("conn.send_messages sent=%s took %.3fs", sent, time.time() - t2)
#         try:
#             conn.close()
#         except Exception:
#             pass

#     except Exception as e:
#         logger.exception("Async EMAIL ERROR: %s", e)
#         traceback.print_exc()


# # def get_in_touch(request):
# #     """
# #     Handles contact form POST and normal GET.
# #     - If POST and request is XHR, returns JsonResponse for inline AJAX form.
# #     - Otherwise uses messages + redirect (existing flow).
# #     """
# #     if request.method == "POST":
# #         name = (request.POST.get("name") or "").strip()
# #         email = (request.POST.get("email") or "").strip()
# #         phone = (request.POST.get("phone") or "").strip()
# #         subject = (request.POST.get("subject") or "Enquiry").strip()
# #         message_text = (request.POST.get("message") or "").strip()

# #         # Basic validation
# #         if not name or not email or not message_text:
# #             msg = "Please complete the required fields."
# #             if request.headers.get("x-requested-with") == "XMLHttpRequest":
# #                 return JsonResponse({"status": "error", "message": msg}, status=400)
# #             messages.error(request, msg)
# #             return redirect("get_in_touch")

# #         admin_subject = f"New contact message from {name}: {subject}"
# #         admin_body = (
# #             f"You received a new message from the website:\n\n"
# #             f"Name: {name}\n"
# #             f"Email: {email}\n"
# #             f"Phone: {phone}\n"
# #             f"Subject: {subject}\n\n"
# #             f"Message:\n{message_text}\n"
# #         )

# #         user_subject = "Thank You for Contacting Us!"
# #         user_body = (
# #             f"Hi {name},\n\n"
# #             "Thank you for reaching out to us. We have received your message and our team will get back to you soon.\n\n"
# #             "If your enquiry is urgent, please contact: +91 907220 05555\n\n"
# #             "Regards,\nPeppe Planet Team"
# #         )

# #         try:
# #             # send both emails in background using one connection
# #             threading.Thread(
# #                 target=_send_two_emails_in_background,
# #                 args=(
# #                     admin_subject,
# #                     admin_body,
# #                     ["online@funridersindia.com"],  # admin recipients
# #                     user_subject,
# #                     user_body,
# #                     [email],  # user auto-reply
# #                 ),
# #                 daemon=True,
# #             ).start()

# #             success_msg = "Your message has been sent successfully. We will contact you soon."
# #             if request.headers.get("x-requested-with") == "XMLHttpRequest":
# #                 return JsonResponse({"status": "ok", "message": success_msg})
# #             messages.success(request, success_msg)

# #         except Exception as exc:
# #             logger.exception("Error while dispatching contact emails: %s", exc)
# #             if request.headers.get("x-requested-with") == "XMLHttpRequest":
# #                 return JsonResponse({"status": "error", "message": "Something went wrong while sending your message."}, status=500)
# #             messages.error(request, "Something went wrong while sending your message.")

# #         return redirect("get_in_touch")

# #     # GET
# #     return render(request, "get_in_touch.html")



# logger = logging.getLogger(__name__)

# def _send_two_emails_in_background(admin_subject, admin_body, admin_recipients,
#                                    user_subject, user_body, user_recipients):
#     # your implementation to send two emails using one SMTP connection
#     # e.g. using django.core.mail.send_mail or EmailMessage
#     pass

# def get_in_touch(request):
#     """
#     Handles contact form POST and normal GET.
#     - If POST and request is XHR, returns JsonResponse for inline AJAX form.
#     - Otherwise uses messages + redirect (existing flow).
#     """
#     if request.method == "POST":
#         name = (request.POST.get("name") or "").strip()
#         email = (request.POST.get("email") or "").strip()
#         phone = (request.POST.get("phone") or "").strip()
#         message_text = (request.POST.get("message") or "").strip()

#         # Basic validation
#         if not name or not email or not message_text:
#             msg = "Please complete the required fields."
#             if request.headers.get("x-requested-with") == "XMLHttpRequest":
#                 return JsonResponse({"status": "error", "message": msg}, status=400)
#             messages.error(request, msg)
#             return redirect("get_in_touch")

#         # Use a fixed subject for admin notifications (form no longer contains subject)
#         admin_subject = f"Website enquiry from {name}"
#         admin_body = (
#             f"You received a new message from the website:\n\n"
#             f"Name: {name}\n"
#             f"Email: {email}\n"
#             f"Phone: {phone}\n\n"
#             f"Message:\n{message_text}\n"
#         )

#         user_subject = "Thank You for Contacting Us!"
#         user_body = (
#             f"Hi {name},\n\n"
#             "Thank you for reaching out to us. We have received your message and our team will get back to you soon.\n\n"
#             "If your enquiry is urgent, please contact: +91 907220 05555\n\n"
#             "Regards,\nPeppe Planet Team"
#         )

#         try:
#             # send both emails in background using one connection
#             threading.Thread(
#                 target=_send_two_emails_in_background,
#                 args=(
#                     admin_subject,
#                     admin_body,
#                     ["online@funridersindia.com"],  # admin recipients
#                     user_subject,
#                     user_body,
#                     [email],  # user auto-reply
#                 ),
#                 daemon=True,
#             ).start()

#             success_msg = "Your message has been sent successfully. We will contact you soon."
#             if request.headers.get("x-requested-with") == "XMLHttpRequest":
#                 return JsonResponse({"status": "ok", "message": success_msg})
#             messages.success(request, success_msg)

#         except Exception as exc:
#             logger.exception("Error while dispatching contact emails: %s", exc)
#             if request.headers.get("x-requested-with") == "XMLHttpRequest":
#                 return JsonResponse({"status": "error", "message": "Something went wrong while sending your message."}, status=500)
#             messages.error(request, "Something went wrong while sending your message.")

#         return redirect("get_in_touch")

#     # GET
#     return render(request, "get_in_touch.html")
import logging
import threading
import time
import traceback

from django.conf import settings
from django.core.mail import send_mail, get_connection, EmailMessage
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

logger = logging.getLogger(__name__)


# ---------- email helpers ----------
def _send_mail_async(subject, message, from_email, recipient_list):
    """Simple wrapper for send_mail in a background thread."""
    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    except Exception:
        logger.exception("Async single send_mail failed")


def _send_two_emails_in_background(admin_subject, admin_body, admin_recipients,
                                   user_subject, user_body, user_recipients):
    """
    Send two EmailMessage objects over a single SMTP connection.
    Intended to be run inside a background thread.
    """
    try:
        t0 = time.time()
        conn = get_connection(
            host=getattr(settings, "EMAIL_HOST", None),
            port=getattr(settings, "EMAIL_PORT", None),
            username=getattr(settings, "EMAIL_HOST_USER", None),
            password=getattr(settings, "EMAIL_HOST_PASSWORD", None),
            use_tls=getattr(settings, "EMAIL_USE_TLS", False),
            use_ssl=getattr(settings, "EMAIL_USE_SSL", False),
            timeout=getattr(settings, "EMAIL_TIMEOUT", None),
        )
        logger.debug("get_connection took %.3fs", time.time() - t0)

        conn.open()
        from_email = getattr(settings, "DEFAULT_FROM_EMAIL", settings.EMAIL_HOST_USER)

        admin_msg = EmailMessage(
            subject=admin_subject,
            body=admin_body,
            from_email=from_email,
            to=admin_recipients,
            connection=conn,
        )

        user_msg = EmailMessage(
            subject=user_subject,
            body=user_body,
            from_email=from_email,
            to=user_recipients,
            connection=conn,
        )

        sent = conn.send_messages([admin_msg, user_msg])
        logger.debug("conn.send_messages returned=%s", sent)
        try:
            conn.close()
        except Exception:
            pass

    except Exception:
        logger.exception("Async EMAIL ERROR while sending two messages")


# ---------- simple page views ----------
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def rides(request):
    return render(request, "rides.html")


def news_and_events(request):
    return render(request, "news_and_events.html")


def careers(request):
    return render(request, "careers.html")


def little_peppe(request):
    return render(request, "little_peppe.html")


def peppe_toys(request):
    return render(request, "peppe_toys.html")


def packages(request):
    return render(request, "packages.html")


def locations(request):
    return render(request, "locations.html")


def enquiry(request):
    return render(request, "enquiry.html")


def base(request):
    return render(request, "base.html")


def testimonials(request):
    return render(request, "testimonials.html")


def homeheader(request):
    return render(request, "homeheader.html")


def homefooter(request):
    return render(request, "homefooter.html")


def peppe_party(request):
    return render(request, "peppe_party.html")


def peppe_cafe(request):
    return render(request, "peppe_cafe.html")


def terms_and_conditions(request):
    return render(request, "terms_and_conditions.html")


def faq(request):
    return render(request, "faq.html")


def privacy_and_policy(request):
    return render(request, "privacy_and_policy.html")


def activities(request):
    return render(request, "activities.html")


def offers(request):
    return render(request, "offers.html")


def peppe_style(request):
    return render(request, "peppe_style.html")


def activities_detail(request):
    return render(request, "activities_detail.html")


# ---------- franchise (example with background email) ----------
def franchise(request):
    if request.method == "POST":
        name = (request.POST.get("name") or "").strip()
        email = (request.POST.get("email") or "").strip()
        phone = (request.POST.get("phone") or "").strip()
        subject = (request.POST.get("subject") or "Franchise Enquiry").strip()
        message_text = (request.POST.get("message") or "").strip()

        admin_subject = f"Franchise enquiry from {name}: {subject}"
        admin_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\n{message_text}"

        user_subject = "Thank you for contacting Peppe Planet"
        user_body = f"Hi {name},\n\nThanks for contacting us. We'll get back to you soon.\n\nRegards,\nPeppe Planet Team"

        try:
            threading.Thread(
                target=_send_two_emails_in_background,
                args=(admin_subject, admin_body, ["online@funridersindia.com"],
                      user_subject, user_body, [email]),
                daemon=True,
            ).start()
            messages.success(request, "Your message has been sent successfully. We will contact you soon.")
        except Exception:
            logger.exception("Franchise email dispatch failed")
            messages.error(request, "Something went wrong while sending your message.")

        return render(request, "franchise.html")

    return render(request, "franchise.html")


# ---------- contact/get_in_touch (AJAX-friendly) ----------
def get_in_touch(request):
    """
    If POST:
      - accepts name, email, phone, message.
      - returns JSON when XHR, otherwise uses messages + redirect.
    If GET: renders the page.
    """
    if request.method == "POST":
        name = (request.POST.get("name") or "").strip()
        email = (request.POST.get("email") or "").strip()
        phone = (request.POST.get("phone") or "").strip()
        message_text = (request.POST.get("message") or "").strip()

        if not name or not email or not message_text:
            msg = "Please complete the required fields."
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"status": "error", "message": msg}, status=400)
            messages.error(request, msg)
            return redirect("get_in_touch")

        admin_subject = f"Website enquiry from {name}"
        admin_body = (
            f"You received a new message from the website:\n\n"
            f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\n"
            f"Message:\n{message_text}\n"
        )

        user_subject = "Thank You for Contacting Us!"
        user_body = (
            f"Hi {name},\n\nThank you for reaching out. We'll be in touch soon.\n\nRegards,\nPeppe Planet Team"
        )

        try:
            threading.Thread(
                target=_send_two_emails_in_background,
                args=(admin_subject, admin_body, ["online@funridersindia.com"],
                      user_subject, user_body, [email]),
                daemon=True,
            ).start()

            success_msg = "Your message has been sent successfully. We will contact you soon."
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"status": "ok", "message": success_msg})
            messages.success(request, success_msg)

        except Exception:
            logger.exception("Error while dispatching contact emails")
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"status": "error", "message": "Something went wrong while sending your message."}, status=500)
            messages.error(request, "Something went wrong while sending your message.")

        return redirect("get_in_touch")

    # GET
    return render(request, "get_in_touch.html")
