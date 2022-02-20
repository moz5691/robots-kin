#! /bin/bash

export PROJECT_ID=
export REGION=
export CONNECTION_NAME=

#gcloud builds submit \
#  --tag gcr.io/$PROJECT_ID/<name> \
#  --project $PROJECT_ID

gcloud run deploy <name> \
  --image gcr.io/$PROJECT_ID/<name>
  --platform managed \
  --region $REGION
  --allow-unauthenticated \
  --add-cloudsql-instances $CONNECTION_NAME
  --project $PROJECT_ID

