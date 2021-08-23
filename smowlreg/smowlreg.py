"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import requests
import string
import sys

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, Boolean, Dict, Float, List, Set, Field, ScopeIds
from xblock.fragment import Fragment

from django.utils.translation import ugettext as _
from django.template import Context, Template

from .utils import render_template, xblock_field_list
from django.conf import settings as DJANGO_SETTINGS
from openedx.core.djangoapps.site_configuration.models import SiteConfiguration
from mock import patch, MagicMock, Mock
from xblock.field_data import FieldData, DictFieldData
from xblock.runtime import Runtime

import logging
log = logging.getLogger(__name__)


class SmowlRegXBlock(XBlock):
    """
    XBlock displaying an iframe, with an anonymous ID passed in argument
    """

    # Fields are defined on the class. You can access them in your code as
    # self.<fieldname>.

    # URL format :
    # {iframe_url}/UserID

    nomEntity = ""

    display_name = String(
        help=_("SMOWL"),
        display_name=_("Component Display Name"),
        # name that appears in advanced settings studio menu
        default=_("SMOWL REGISTER"),
        scope=Scope.user_state
    )

    smowlreg_url = String(
        display_name=_("SMOWL ACTIVATED"),
        help=_("PUBLISH to activate SMOWL"),
        default="a",
        scope=Scope.settings
    )

    has_author_view = True

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")
    
    def author_view(self, context=None):
        lms_base = SiteConfiguration.get_value_for_org(
            self.location.org,
            "LMS_BASE",
            DJANGO_SETTINGS.LMS_BASE
        )
        context = {
            'has_settings': self.check_settings(),
            'help_url': 'https://{}/{}'.format(lms_base, 'contact_form')
        }
        frag = Fragment()
        frag.add_content(render_template(
            '/templates/html/smowlreg-author.html', context))
        frag.add_css(self.resource_string("static/css/smowlreg.css"))
        frag.initialize_js('SmowlRegXBlock')
        return frag

    def student_view(self, context=None):
        """
        The primary view of the SMOWLREG, shown to students
        when viewing courses.
        """

        #runtime = TestRuntime(services={'field-data': DictFieldData({})})
        #block = SmowlRegXBlock(runtime, scope_ids=Mock(spec=ScopeIds))
        #parent = block.get_parent()

        #url_response = self.request.GET

        # student es la id del curso y sirve pa saber si es admin
        student_id = self.xmodule_runtime.anonymous_student_id
        user_id = self.scope_ids.user_id

        course_id = self.xmodule_runtime.course_id

        #entityName3 = str(self.course_id).split(":")
        #entityName33 = entityName3[1]
        #entityName2 = str(entityName33).split("+")
        #entityName22 = entityName2[0]
        #entityName = str(entityName22)
        #entityName = 'TRIALCLUCHILE'

        # usage es el codigo del curso mejor asi
        #usage5555 = self.scope_ids.usage_id

        idUnit2 = self.parent
        idUnit = str(idUnit2).split("@")[-1]
        #idUnit5 = "{0}".format(idUnit)

        # new_smowlreg_url = "{0}={1}&course_CourseName={2}".format(self.smowlreg_url, student_id, course_id)
        new_smowlreg_url = "a"

        # QUITAR
        #self.display_name = new_smowlreg_url
        if self.check_settings():
            context = {
                'self': self,
                'location': str(self.location).split('@')[-1],
                'checkBBLink': DJANGO_SETTINGS.SMOWLREG_CHECKBBLINK,
                'has_settings': True           
            }
            settings = {
                'location': str(self.location).split('@')[-1],
                'user_id': self.scope_ids.user_id,
                'course_id': self.course_id,
                'smowlreg_url': new_smowlreg_url,
                'controllerReg_link': DJANGO_SETTINGS.SMOWLREG_CONTROLLER_REG_FULL_URL,
                'has_settings': True
            }
        else:
            context = {
                'has_settings': False           
            }
            settings = {
                'has_settings': False
            }
        frag = Fragment()
        frag.add_content(render_template(
            '/templates/html/smowlreg.html', context))
        frag.add_css(self.resource_string("static/css/smowlreg.css"))
        frag.add_javascript(self.resource_string("static/js/src/smowlreg.js"))
        frag.initialize_js('SmowlRegXBlock', json_args=settings)
        return frag

    def studio_view(self, context=None):
        """
        The studio view of the SMOWLREG, with form
        """
        frag = Fragment()
        frag.add_content(render_template(
            '/templates/html/smowlreg-edit.html'))
        frag.add_javascript(self.resource_string(
            "static/js/src/smowlreg-edit.js"))
        frag.initialize_js('SmowlRegXBlock')
        return frag

    def check_settings(self):
        return (
            hasattr(DJANGO_SETTINGS, 'SMOWLREG_CONTROLLER_REG_BASE_URL') and 
            hasattr(DJANGO_SETTINGS, 'SMOWLREG_CONTROLLER_REG_FULL_URL') and 
            hasattr(DJANGO_SETTINGS, 'SMOWLREG_CHECKBBLINK') and 
            hasattr(DJANGO_SETTINGS, 'SMOWLREG_CHECKBBLINK_FULL_URL') and 
            hasattr(DJANGO_SETTINGS, 'SMOWL_KEY') and 
            hasattr(DJANGO_SETTINGS, 'SMOWL_ENTITY')
            )

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("SmowlRegXBlock",
             """
			 """),
        ]
