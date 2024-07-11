import json
import random

from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.views.generic import RedirectView

from distro.apps.users.models import User
from distro.apps.artists.models import Artist
from distro.apps.tracks.models import Track


def dashboard_callback(request, context):
    WEEKDAYS = [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun",
    ]

    positive = [[1, random.randrange(8, 28)] for i in range(1, 28)]
    negative = [[-1, -random.randrange(8, 28)] for i in range(1, 28)]
    average = [r[1] - random.randint(3, 5) for r in positive]
    performance_positive = [[1, random.randrange(8, 28)] for i in range(1, 28)]
    performance_negative = [[-1, -random.randrange(8, 28)] for i in range(1, 28)]

    context.update(
        {
            "navigation": [
                {"title": _("Dashboard"), "link": "/", "active": True},
                {"title": _("Analytics"), "link": "#"},
                {"title": _("Settings"), "link": "#"},
            ],
            "filters": [
                {"title": _("All"), "link": "#", "active": True},
                {
                    "title": _("New"),
                    "link": "#",
                },
            ],
           "numbers": [
                {
                    "title": "Users",
                    "metric": User.objects.count(),
                    "footer": '',
                },
                {
                    "title": "Artists",
                    "metric": Artist.objects.count(),
                    "footer": '',
                },
                {
                    "title": "Tracks",
                    "metric": Track.objects.count(),
                    "footer": '',
                },
            ], 
            "kpi": [
                {
                    "title": "Artist A Performance",
                    "metric": "$144.54",
                    "footer": mark_safe(
                        '<strong class="text-green-600 font-medium">+3.14%</strong>&nbsp;progress from last week'
                    ),
                    "chart": json.dumps(
                        {
                            "labels": [WEEKDAYS[day % 7] for day in range(1, 28)],
                            "datasets": [{"data": average, "borderColor": "#9333ea"}],
                        }
                    ),
                },
                {
                    "title": "Artist B Performance",
                    "metric": "$234.56",
                    "footer": mark_safe(
                        '<strong class="text-green-600 font-medium">-2.14%</strong>&nbsp;progress from last week'
                    ),
                },
                {
                    "title": "Artist C Performance",
                    "metric": "$34.56",
                    "footer": mark_safe(
                        '<strong class="text-green-600 font-medium">+1.18%</strong>&nbsp;progress from last week'
                    ),
                },
            ], 
            "progress": [
                {
                    "title": "Spotify",
                    "description": " $3,234.56",
                    "value": random.randint(10, 90),
                },
                {
                    "title": "Youtube Music",
                    "description": " $1,234.56",
                    "value": random.randint(10, 90),
                },
                {
                    "title": "Amazon Music",
                    "description": " $1,234.56",
                    "value": random.randint(10, 90),
                },
                {
                    "title": "Pandora",
                    "description": " $234.56",
                    "value": random.randint(10, 90),
                },
                {
                    "title": "Other income",
                    "description": " $1,234.56",
                    "value": random.randint(10, 90),
                },
            ],
            "chart": json.dumps(
                {
                    "labels": [WEEKDAYS[day % 7] for day in range(1, 28)],
                    "datasets": [
                        {
                            "label": "Example 1",
                            "type": "line",
                            "data": average,
                            "backgroundColor": "#f0abfc",
                            "borderColor": "#f0abfc",
                        },
                        {
                            "label": "Example 2",
                            "data": positive,
                            "backgroundColor": "#9333ea",
                        },
                        {
                            "label": "Example 3",
                            "data": negative,
                            "backgroundColor": "#f43f5e",
                        },
                    ],
                }
            ),
            "performance": [
                {
                    "title": _("Last week revenue"),
                    "metric": "$1,234.56",
                    "footer": mark_safe(
                        '<strong class="text-green-600 font-medium">+3.14%</strong>&nbsp;progress from last week'
                    ),
                    "chart": json.dumps(
                        {
                            "labels": [WEEKDAYS[day % 7] for day in range(1, 28)],
                            "datasets": [
                                {"data": performance_positive, "borderColor": "#9333ea"}
                            ],
                        }
                    ),
                },
                {
                    "title": _("Last week expenses"),
                    "metric": "$1,234.56",
                    "footer": mark_safe(
                        '<strong class="text-green-600 font-medium">+3.14%</strong>&nbsp;progress from last week'
                    ),
                    "chart": json.dumps(
                        {
                            "labels": [WEEKDAYS[day % 7] for day in range(1, 28)],
                            "datasets": [
                                {"data": performance_negative, "borderColor": "#f43f5e"}
                            ],
                        }
                    ),
                },
            ],
        },
    )

    return context
