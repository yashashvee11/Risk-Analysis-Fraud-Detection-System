from dashboard.utils import execute
from dashboard.models import Document
from dashboard.utils import transformResponse
from django.shortcuts import redirect, render
import time, os, csv
from dashboard.utils import process_csv


# def is_csv(content):
#     """Check if the content is CSV by trying to parse it."""
#     try:
#         # Read first few lines to check CSV structure
#         lines = content.splitlines()
#         sample = csv.reader(lines)
#         next(sample)  # Try reading the first row
#         return True
#     except Exception:
#         return False


# def dashboardView(request):
#     if request.method == "GET":
#         return redirect("homeView")

#     if request.method == "POST":
#         lastestDoc = Document.objects.last()

#         if not lastestDoc:
#             return render(request, "dashboard.html", {"error": "No document found"})

#         print(lastestDoc.content)

#         # **Check if the document is CSV**
#         if is_csv(lastestDoc.content):
#             print("Detected CSV file, applying CSV function...")
#             response = process_csv(lastestDoc.content)  # Apply your CSV function
#             response = execute(response, True)
#             print(f"Response: {response}")
#         else:
#             response = execute(lastestDoc.content)

#         context = transformResponse(response)
#         print(f"****{context}*****")
#         print("I am in dashboardView POST")
#         return render(request, "dashboard.html", context)


def dashboardView(request):
    if request.method == "GET":
        return redirect("homeView")
    if request.method == "POST":
        lastestDoc = Document.objects.last()
        # time.sleep(3)
        print(lastestDoc.content)
        response = execute(lastestDoc.content)
        context = transformResponse(response)
        print(f"****{context}*****")
        print("I am in dashboardView POST")
        return render(request, "dashboard.html", context)


def homeView(request):
    context = {}
    if request.method == "GET":
        return render(request, "home.html", context)

    if request.method == "POST":
        # time.sleep(3)
        doc = Document(
            document=request.FILES.get("file"),
            dataType=request.POST.get("dataType"),
            content=request.FILES.get("file").read().decode("utf-8"),
        )
        doc.save()
        return render(request, "home.html", context)
