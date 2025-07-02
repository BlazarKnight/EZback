# EZback GTK4 Application - Maintenance Guide

## Overview
This guide covers maintaining your GTK4 Python application that uses Gtk.Template for UI definition. The app creates a backup utility interface with multiple buttons and an image display.

## Code Structure

### Main Components
- **XML Template**: Defines the UI layout using GTK4's template system
- **Foo Class**: Main widget class that inherits from Gtk.Box
- **Application Setup**: Standard GTK4 application initialization

### Key Files Referenced
- `src/icon/EZbackicon2.04-8.png` - Main application icon
- `Learn.gresource` - Optional resource bundle (loaded if available)

## Common Maintenance Tasks

### Adding New Buttons
1. **In XML Template**: Add a new `<child>` section with a `GtkButton` object
2. **In Python Class**: Add corresponding `@Gtk.Template.Callback()` method
3. **Example**:
   ```xml
   <child>
     <object class="GtkButton" id="restore_button">
       <property name="label">Restore Backup</property>
       <signal name="clicked" handler="restore_button_clicked" swapped="no" />
       <property name="margin-bottom">6</property>
     </object>
   </child>
   ```
   ```python
   @Gtk.Template.Callback()
   def restore_button_clicked(self, button):
       print("Restore backup clicked")
   ```

### Modifying Layout
- **Spacing**: Adjust `spacing` property in the main GtkBox
- **Margins**: Modify `margin-top`, `margin-bottom`, `margin-start`, `margin-end`
- **Button spacing**: Change individual button `margin-bottom` values
- **Image size**: Adjust `pixel-size` property (currently 150px)

### Updating Images
1. Replace the file at `src/icon/EZbackicon2.04-8.png`
2. Or change the `file` property in the GtkImage object
3. Supported formats: PNG, JPG, SVG, GIF

### Window Properties
Modify in the `on_activate()` function:
- **Size**: `win.set_default_size(width, height)`
- **Title**: `win.set_title("Your Title")`
- **Resizable**: `win.set_resizable(False)` to lock size

## Troubleshooting Guide

### Common Issues

#### Buttons Not Appearing
- **Cause**: Conflicting widget creation in `__init__`
- **Fix**: Only call `super().__init__()`, let template handle widgets

#### Template Loading Errors
- **Cause**: Malformed XML or wrong property names
- **Fix**: Validate XML structure, use kebab-case for properties (`can-focus`, not `can_focus`)

#### Signal Connection Failures
- **Cause**: Missing callback methods or wrong signal names
- **Fix**: Ensure every button has a corresponding `@Gtk.Template.Callback()` method

#### Image Not Loading
- **Cause**: File path incorrect or file doesn't exist
- **Fix**: Verify file exists at specified path, use absolute paths if needed

#### Resource Loading Issues
- **Cause**: `Learn.gresource` file missing
- **Fix**: Code handles this gracefully with try/catch block

### Debugging Tips
1. **Check console output** for error messages
2. **Test button clicks** - each should print a message
3. **Verify file paths** for images and resources
4. **Use GTK Inspector** (`GTK_DEBUG=interactive python your_app.py`)

## Best Practices

### Code Organization
- Keep XML template at the top for easy editing
- Group related callback methods together
- Use descriptive button IDs and handler names

### Property Naming
- Use kebab-case in XML: `can-focus`, `pixel-size`, `margin-bottom`
- Use snake_case in Python: `hello_button_clicked`

### Error Handling
- Wrap resource loading in try/catch blocks
- Check file existence before loading images
- Provide fallbacks for missing assets

### Performance
- Keep image sizes reasonable (150-300px for icons)
- Don't create widgets manually when using templates
- Use appropriate container widgets (Box vs Grid vs etc.)

## Documentation Resources

### Official GTK Documentation
- **GTK4 Documentation**: https://docs.gtk.org/gtk4/
- **Python GI Documentation**: https://pygobject.readthedocs.io/
- **Adwaita Guidelines**: https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/

### Key Reference Pages
- **Gtk.Template**: https://docs.gtk.org/gtk4/class.Template.html
- **Gtk.Box**: https://docs.gtk.org/gtk4/class.Box.html
- **Gtk.Button**: https://docs.gtk.org/gtk4/class.Button.html
- **Gtk.ApplicationWindow**: https://docs.gtk.org/gtk4/class.ApplicationWindow.html
- **Signal Handling**: https://docs.gtk.org/gobject/concepts.html#signals

### Python-Specific Resources
- **PyGObject Tutorial**: https://python-gtk-3-tutorial.readthedocs.io/
- **GI Repository**: https://pygobject.readthedocs.io/en/latest/guide/api/index.html

### Community Resources
- **GTK Discourse**: https://discourse.gnome.org/c/platform/5
- **Stack Overflow**: Search for "gtk4 python" or "pygobject"
- **GNOME GitLab**: https://gitlab.gnome.org/GNOME/gtk

### Tools
- **GTK Inspector**: Built-in debugging tool (`GTK_DEBUG=interactive`)
- **Glade**: Visual UI designer (though this code uses string templates)
- **devhelp**: GNOME documentation browser

## Version Compatibility
- **GTK Version**: 4.0+
- **Python**: 3.6+
- **PyGObject**: 3.30+
- **Adwaita**: 1.0+ (if using Adw widgets)

## Future Enhancements
Consider these improvements:
- Add proper error dialogs instead of console prints
- Implement actual backup functionality
- Add configuration file support
- Create proper application icons and desktop files
- Add keyboard shortcuts
- Implement progress bars for long operations