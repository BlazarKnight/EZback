import gi
import os

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, Gio, GLib

# Fixed XML template - removed ScrolledWindow, made image smaller
xml_of_welcome = """\
<interface>
  <template class="wigit" parent="GtkBox">
    <child>
      <object class="GtkBox">
        <property name="orientation">vertical</property>
        <property name="spacing">10</property>
        <property name="margin-top">20</property>
        <property name="margin-bottom">20</property>
        <property name="margin-start">20</property>
        <property name="margin-end">20</property>
        <child>
          <object class="GtkLabel">
            <property name="label" translatable="yes">Welcome to EZback</property>
            <property name="margin-bottom">10</property>
            <style>
              <class name="title-1"/>
            </style>
          </object>
        </child>
        <child>
          <object class="GtkImage">
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="file">src/icon/EZbackicon2.04-8.png</property>
            <property name="pixel-size">150</property>
          </object>
        </child>
        <child>
          <object class="GtkLabel">
            <property name="label">back up software made EZ</property>
            <property name="justify">center</property>
            <property name="margin-bottom">20</property>
          </object>
        </child>
        <child>
          <object class="GtkButton" id="hello_button">
            <property name="label">Hello World</property>
            <signal name="clicked" handler="hello_button_clicked" swapped="no" />
            <property name="margin-bottom">6</property>
          </object>
        </child>
        <child>
          <object class="GtkButton" id="New">
            <property name="label">Make a new backup</property>
            <signal name="clicked" handler="new_button_clicked" swapped="no" />
            <property name="margin-bottom">6</property>
          </object>
        </child>
        <child>
          <object class="GtkButton" id="Update">
            <property name="label">Update old backup</property>
            <signal name="clicked" handler="update_button_clicked" swapped="no" />
            <property name="margin-bottom">6</property>
          </object>
        </child>
        <child>
          <object class="GtkButton" id="Verify">
            <property name="label">Verify backup integrity</property>
            <signal name="clicked" handler="verify_button_clicked" swapped="no" />
            <property name="margin-bottom">6</property>
          </object>
        </child>
        <child>
          <object class="GtkButton" id="About">
            <property name="label">About EZback</property>
            <signal name="clicked" handler="about_button_clicked" swapped="no" />
            <property name="margin-bottom">6</property>
          </object>
        </child>
      </object>
    </child>
  </template>
</interface>
"""
about_dialog_xml = """\
<interface>
  <template class="AboutDialogWidget" parent="GtkBox">
    <property name="orientation">vertical</property>
    <property name="spacing">15</property>
    <property name="margin-top">30</property>
    <property name="margin-bottom">30</property>
    <property name="margin-start">40</property>
    <property name="margin-end">40</property>
    <property name="halign">center</property>

    <!-- App Icon -->
    <child>
      <object class="GtkImage" id="app_icon">
        <property name="file">src/icon/EZbackicon2.04-8.png</property>
        <property name="pixel-size">128</property>
        <property name="margin-bottom">10</property>
      </object>
    </child>

    <!-- App Name -->
    <child>
      <object class="GtkLabel">
        <property name="label">EZback</property>
        <property name="margin-bottom">5</property>
        <style>
          <class name="title-1"/>
        </style>
      </object>
    </child>

    <!-- Version -->
    <child>
      <object class="GtkLabel" id="version_label">
        <property name="label">Version 1.0.0</property>
        <property name="margin-bottom">15</property>
        <style>
          <class name="dim-label"/>
        </style>
      </object>
    </child>

    <!-- Description -->
    <child>
      <object class="GtkLabel">
        <property name="label">Backup software made EZ</property>
        <property name="justify">center</property>
        <property name="margin-bottom">10</property>
        <style>
          <class name="heading"/>
        </style>
      </object>
    </child>

    <!-- Detailed Description -->
    <child>
      <object class="GtkLabel">
        <property name="label">A simple, efficient, and user-friendly backup solution.
Create, update, and verify your backups with ease.
Keep your important data safe and secure.</property>
        <property name="justify">center</property>
        <property name="wrap">true</property>
        <property name="max-width-chars">50</property>
        <property name="margin-bottom">20</property>
      </object>
    </child>

    <!-- Info Grid -->
    <child>
      <object class="GtkGrid" id="info_grid">
        <property name="row-spacing">8</property>
        <property name="column-spacing">20</property>
        <property name="halign">center</property>
        <property name="margin-bottom">20</property>

        <!-- Copyright -->
        <child>
          <object class="GtkLabel">
            <property name="label">Copyright:</property>
            <property name="halign">end</property>
            <style>
              <class name="dim-label"/>
            </style>
            <layout>
              <property name="column">0</property>
              <property name="row">0</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="GtkLabel">
            <property name="label">© 2025 Your Name</property>
            <property name="halign">start</property>
            <layout>
              <property name="column">1</property>
              <property name="row">0</property>
            </layout>
          </object>
        </child>

        <!-- License -->
        <child>
          <object class="GtkLabel">
            <property name="label">License:</property>
            <property name="halign">end</property>
            <style>
              <class name="dim-label"/>
            </style>
            <layout>
              <property name="column">0</property>
              <property name="row">1</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="GtkLabel">
            <property name="label">GPL v3.0</property>
            <property name="halign">start</property>
            <layout>
              <property name="column">1</property>
              <property name="row">1</property>
            </layout>
          </object>
        </child>

        <!-- Built with -->
        <child>
          <object class="GtkLabel">
            <property name="label">Built with:</property>
            <property name="halign">end</property>
            <style>
              <class name="dim-label"/>
            </style>
            <layout>
              <property name="column">0</property>
              <property name="row">2</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="GtkLabel">
            <property name="label">Python &amp; GTK4</property>
            <property name="halign">start</property>
            <layout>
              <property name="column">1</property>
              <property name="row">2</property>
            </layout>
          </object>
        </child>
      </object>
    </child>

    <!-- Links Section -->
    <child>
      <object class="GtkBox">
        <property name="orientation">horizontal</property>
        <property name="spacing">10</property>
        <property name="halign">center</property>
        <property name="margin-bottom">20</property>

        <child>
          <object class="GtkButton" id="website_button">
            <property name="label">Visit Website</property>
            <signal name="clicked" handler="on_website_clicked" swapped="no" />
            <style>
              <class name="flat"/>
            </style>
          </object>
        </child>

        <child>
          <object class="GtkSeparator">
            <property name="orientation">vertical</property>
          </object>
        </child>

        <child>
          <object class="GtkButton" id="github_button">
            <property name="label">Source Code</property>
            <signal name="clicked" handler="on_github_clicked" swapped="no" />
            <style>
              <class name="flat"/>
            </style>
          </object>
        </child>

        <child>
          <object class="GtkSeparator">
            <property name="orientation">vertical</property>
          </object>
        </child>

        <child>
          <object class="GtkButton" id="report_button">
            <property name="label">Report Issue</property>
            <signal name="clicked" handler="on_report_clicked" swapped="no" />
            <style>
              <class name="flat"/>
            </style>
          </object>
        </child>
      </object>
    </child>

    <!-- Credits -->
    <child>
      <object class="GtkLabel">
        <property name="label">Special thanks to the GTK and Python communities</property>
        <property name="justify">center</property>
        <property name="margin-bottom">20</property>
        <style>
          <class name="dim-label"/>
          <class name="caption"/>
        </style>
      </object>
    </child>

    <!-- Close Button -->
    <child>
      <object class="GtkButton" id="close_button">
        <property name="label">Close</property>
        <property name="halign">center</property>
        <property name="width-request">100</property>
        <signal name="clicked" handler="on_close_clicked" swapped="no" />
        <style>
          <class name="suggested-action"/>
        </style>
      </object>
    </child>
  </template>
</interface>
"""

# Load resource if it exists
try:
    resource = Gio.Resource.load('Learn.gresource')
    Gio.resources_register(resource)
except:
    print("Resource file not found, continuing without it")


# Template class for the About dialog
@Gtk.Template(string=about_dialog_xml)
class AboutDialogWidget(Gtk.Box):
    __gtype_name__ = "AboutDialogWidget"

    # Get references to widgets
    app_icon = Gtk.Template.Child()
    version_label = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
        self.setup_dynamic_content()

    def setup_dynamic_content(self):
        """Set up dynamic content like version info"""
        # You can update version dynamically
        import datetime
        build_date = datetime.datetime.now().strftime("%B %Y")
        self.version_label.set_text(f"Version 1.0.0 • Built {build_date}")

    @Gtk.Template.Callback()
    def on_website_clicked(self, button):
        """Open website URL"""
        self.open_url("https://github.com/yourusername/ezback")

    @Gtk.Template.Callback()
    def on_github_clicked(self, button):
        """Open GitHub repository"""
        self.open_url("https://github.com/yourusername/ezback")

    @Gtk.Template.Callback()
    def on_report_clicked(self, button):
        """Open issue reporting page"""
        self.open_url("https://github.com/yourusername/ezback/issues")

    def open_url(self, url):
        """Open URL in default browser"""
        try:
            import webbrowser
            webbrowser.open(url)
        except Exception as e:
            print(f"Could not open URL {url}: {e}")
            # Show a dialog with the URL
            self.show_url_dialog(url)

    def show_url_dialog(self, url):
        """Show dialog with URL if browser opening fails"""
        dialog = Gtk.MessageDialog(
            transient_for=self.get_root(),
            modal=True,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Visit Website"
        )
        dialog.set_secondary_text(f"Please visit: {url}")
        dialog.connect("response", lambda d, r: d.destroy())
        dialog.present()

    @Gtk.Template.Callback()
    def on_close_clicked(self, button):
        """Close the about dialog"""
        self.get_root().destroy()


# Function to create and show the About dialog
def show_about_dialog(parent_app):
    """Create and show About dialog window"""
    window = Gtk.ApplicationWindow(application=parent_app)
    window.set_title("About EZback")
    window.set_default_size(450, 600)
    window.set_resizable(False)
    window.set_modal(True)

    # Create the widget from template
    about_widget = AboutDialogWidget()
    window.set_child(about_widget)

    window.present()
    return window


@Gtk.Template(string=xml_of_welcome)
class Foo(Gtk.Box):
    __gtype_name__ = "wigit"

    def __init__(self):
        super().__init__()
        # Don't set orientation here - template handles it
        # Don't create buttons manually - template defines them

    @Gtk.Template.Callback()
    def hello_button_clicked(self, button):
        print("Hello world from template button")

    @Gtk.Template.Callback()
    def new_button_clicked(self, button):
        print("New backup clicked")

    @Gtk.Template.Callback()
    def update_button_clicked(self, button):
        print("Update backup clicked")

    @Gtk.Template.Callback()
    def verify_button_clicked(self, button):
        print("Verify backup clicked")

    @Gtk.Template.Callback()
    def about_button_clicked(self, button):
        # Show custom About dialog
        app = self.get_root().get_application()
        show_about_dialog(app)


def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.set_title("EZback")
    win.set_default_size(500, 700)  # Made window taller

    # Use only the template widget
    widget = Foo()
    win.set_child(widget)
    win.present()


# Create application
app = Gtk.Application(application_id='com.example.EZback')
app.connect('activate', on_activate)

if __name__ == '__main__':
    app.run(None)