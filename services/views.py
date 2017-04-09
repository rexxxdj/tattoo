# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
    services = (
    	{'id': 1,
    	'name': u'Художественная татуировка',
    	'description': u'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, interdum justo suscipit id.',
		'image' : 'img/service_tatoo.jpg'
		},
		{'id': 2,
		'name': u'Татуаж',
		'description': u'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, interdum justo suscipit id.',
		'image' : 'img/service_tatooag.jpg'
		},
		{'id': 3,
		'name': u'Микроблейдинг',
		'description': u'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, interdum justo suscipit id.',
		'image' : 'img/service_micro.jpg'
		},
		{'id': 4,
		'name': u'Пирсинг',
		'description': u'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, interdum justo suscipit id.',
		'image' : 'img/service_pircing.jpg'
		}
		)
    team = (
		{'id': 1,
		'name': u'Ben Johnson',
		'title': u'Musician',
		'photo': 'img/1.jpg',
		'description': u'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, et interdum justo suscipit id. Etiam dictum feugiat tellus, a semper massa.',
		'vk': '#',
		'acebook': '#',
		'twitter': '#',
		'instagram': '#'
		},
		{'id': 2,
		'name': u'Emily Clark',
		'title': u'Artist',
		'photo': 'img/2.jpg',
		'description': u'Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, et interdum justo suscipit id. Etiam dictum feugiat tellus, a semper massa.',
		'vk': '#',
		'facebook': '#',
		'twitter': '#',
		'instagram': '#'
		},
		{'id': 3,
		'name': u'Carl Kent',
		'title': u'Stylist',
		'photo': 'img/3.jpg',
		'description': u'Anean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, et interdum justo suscipit id. Etiam dictum feugiat tellus, a semper massa.',
		'vk': '#',
		'facebook': '#',
		'twitter': '#',
		'instagram': '#'
		}
		)
    gallery = (
    	{'id': 1,
    	'photo': 'img/tatoo/bear.jpg'
    	},
    	{'id': 2,
    	'photo': 'img/tatoo/october.jpg'
    	},
    	{'id': 3,
    	'photo': 'img/tatoo/clock.jpg'
    	},
    	{'id': 4,
    	'photo': 'img/tatoo/polka.jpg'
    	},
    	{'id': 5,
    	'photo': 'img/tatoo/samurai.jpg'
    	},
    	{'id': 6,
    	'photo': 'img/tatoo/volna.jpg'
    	}
    	)
    return render(request, 'index.html', 
    	{'services': services, 'team': team, 
    	'gallery': gallery})

def service_list(request):
	return render(request, 'services.html', {})

# Create your views here.
