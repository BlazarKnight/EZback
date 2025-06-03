xml = """\
<interface>
  <template class="wigit" parent="GtkBox">
  <child>
  <object class="GtkScrollable">
  <child>
      <object class="GtkLabel">
        <property name="label" translatable="yes">Welcome to EZback</property>
        <property name="margin-bottom">3</property>
        <style>
          <class name="title-1"/>
        </style>
      </object>
    </child>
    <child>
          <object class="GtkImage">
  <property name="visible">True</property>
  <property name="can_focus">True</property>
  <property name="file">src/icon/EZbackicon2.04-8.png</property>
  <property name="pixel_size">500</property>
</object>

        </child>
    <child>
          <object class="GtkLabel">
            <property name="label">back up softwear made EZ </property>
            <property name="justify">2</property>
          </object>
        </child>
      <child>
      <object class="GtkButton" id="hello_button">
        <property name="label">Hello World</property>
        <signal name="clicked" handler="hello_button_clicked" swapped="no" />
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
import gi
import os
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, Gio, GLib



#base_path = os.path.abspath(os.path.dirname(__file__))
#resource_path = os.path('Learn.gresource')
resource = Gio.Resource.load('Learn.gresource')




uifile="src/ui/this works.ui"
@Gtk.Template(string=xml)
class Foo(Gtk.Box):
    __gtype_name__ = "wigit"

    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)

        self.hello_button = Gtk.Button(label="EZback")
        self.hello_button.connect('clicked', self.hello_button_clicked)
        self.append(self.hello_button)

        image = Gtk.Image.new_from_file('src/icon/EZbackicon2.04-8.svg')




    @Gtk.Template.Callback()
    def hello_button_clicked(self, *args):
        print("hello world from temp")






def on_activate(app):
    # … create a new window…
    win = Gtk.ApplicationWindow(application=app)
    # … with a button in it…
    btn = Gtk.Button(label='Hello, World!')
    # … which closes the window when clicked
    btn.connect('clicked', lambda x: print("hello world from py"))
    win.set_child(Foo())
    win.present()

# Create a new application
app = Gtk.Application(application_id='com.example.GtkApplication')
app.connect('activate', on_activate)

# Run the application



if __name__ == '__main__':

    app.run(None)