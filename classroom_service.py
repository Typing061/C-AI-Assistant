import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/classroom.courses.readonly"]


def get_service():
    creds = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("classroom", "v1", credentials=creds)
    return service


def get_courses():
    service = get_service()
    results = service.courses().list().execute()
    return results.get("courses", [])


def get_assignments(course_id):
    service = get_service()
    results = service.courses().courseWork().list(courseId=course_id).execute()
    return results.get("courseWork", [])