# EDL Server for Palo Alto Networks

This project provides a Django REST Framework web application that serves as an External Dynamic List (EDL) server for Palo Alto Networks appliances. The application allows you to manage custom blocklists of IPs or domains and exposes them as JSON for use by the firewall.

## Table of Contents
- [EDL Server for Palo Alto Networks](#edl-server-for-palo-alto-networks)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
    - [Create a Virtual Environment](#create-a-virtual-environment)
    - [Install Dependencies](#install-dependencies)
    - [Create a New Django Project](#create-a-new-django-project)
    - [Create a New Django App](#create-a-new-django-app)
    - [Configure the Database](#configure-the-database)
    - [Define the EDL Model](#define-the-edl-model)
    - [Create the API Endpoint](#create-the-api-endpoint)
  - [Running the Server](#running-the-server)
  - [Testing the API](#testing-the-api)
  - [Configuring Palo Alto Networks Firewall](#configuring-palo-alto-networks-firewall)

## Prerequisites

- Python 3
- Django
- Django REST Framework

## Setup

### Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install django djangorestframework
```

### Create a New Django Project

```bash
django-admin startproject django_project .
```

### Create a New Django App

```bash
python manage.py startapp api
```

### Configure the Database

Update the `INSTALLED_APPS` section in the `settings.py` file to include the `rest_framework` and `api` apps:

```python
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "rest_framework",
        "api",
    ]
```

### Define the EDL Model

Create the `models.py` file in the "api" app directory with the following content:

```python
    from django.db import models

    class EDLEntry(models.Model):
        ENTRY_TYPE_CHOICES = [
            ('IP', 'IP Address'),
            ('DOMAIN', 'Domain Name'),
        ]
        entry_type = models.CharField(max_length=10, choices=ENTRY_TYPE_CHOICES)
        entry_value = models.CharField(max_length=255)
        is_active = models.BooleanField(default=True)

        def __str__(self):
            return self.entry_value
```

### Create the API Endpoint

Refer to [Step 5](#step-5-create-a-serializerspy-urlspy-and-viewspy-to-expose-our-tables-contents-as-json) and [Step 6](#step-6-test-our-web-applications-api-for-presenting-the-edl-information) for instructions on creating the API endpoint.

## Running the Server

Start the Django development server:

```bash
python manage.py runserver
```

## Testing the API

Refer to [Step 6](#step-6-test-our-web-applications-api-for-presenting-the-edl-information) for instructions on testing the API.

## Configuring Palo Alto Networks Firewall

Refer to [Step 7](#step-7-configure-our-palo-alto-networks-environment-to-talk-to-the-edl-server-for-blacklisted-ips-or-domains) for instructions on configuring the Palo Alto Networks firewall to use the EDL server.
