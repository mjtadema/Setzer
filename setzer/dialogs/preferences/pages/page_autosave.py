#!/usr/bin/env python3
# coding: utf-8

# Copyright (C) 2017-present Robert Griesel
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class PageAutosave(object):

    def __init__(self, preferences, settings, workspace):
        self.view = PageAutosaveView()
        self.preferences = preferences
        self.settings = settings
        self.workspace = workspace

    def init(self):
        self.view.option_autosave.set_active(self.settings.get_value('preferences', 'enable_autosave'))
        self.view.option_autosave.connect('toggled', self.preferences.on_check_button_toggle, 'enable_autosave')
        self.view.option_autosave.connect('toggled', self.workspace.init_autosave_timeout, 'enable_autosave')

        self.view.autosave_interval_spinbutton.set_value(self.settings.get_value('preferences', 'autosave_interval'))
        self.view.autosave_interval_spinbutton.connect('value-changed', self.preferences.spin_button_changed, 'autosave_interval')
        self.view.autosave_interval_spinbutton.connect('value-changed', self.workspace.init_autosave_timeout,
                                                       'autosave_interval')

class PageAutosaveView(Gtk.Box):

    def __init__(self):
        Gtk.Box.__init__(self)
        self.set_orientation(Gtk.Orientation.VERTICAL)

        self.set_margin_start(18)
        self.set_margin_end(18)
        self.set_margin_top(18)
        self.set_margin_bottom(18)
        self.get_style_context().add_class('preferences-page')

        label = Gtk.Label()
        label.set_markup('<b>' + _('Autosave') + '</b>')
        label.set_xalign(0)
        label.set_margin_bottom(6)
        self.append(label)

        self.option_autosave = Gtk.CheckButton.new_with_label(_('Enable autosave'))
        self.append(self.option_autosave)

        label = Gtk.Label()
        label.set_markup(_('Set Autosave Interval in minutes:'))
        label.set_xalign(0)
        label.set_margin_top(18)
        label.set_margin_bottom(6)
        self.append(label)
        box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 0)
        self.autosave_interval = Gtk.SpinButton.new_with_range(5, 30, 5)
        box.append(self.autosave_interval)
        self.append(box)


