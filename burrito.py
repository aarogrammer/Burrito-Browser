#!/usr/bin/env python
import pygtk
pygtk.require('2.0') #require version 2.0+
import gtk
import webkit
import gobject
class Burrito:
    default_site = "http://aaron-welsh.co.uk/burrito/index.html"
    def delete_event(self, widget, event, data=None):
        return False
    def destroy(self, widget, data=None):
        gtk.main_quit()
        print("Burrito has closed...")
    def __init__(self):
        gobject.threads_init()
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_resizable(True)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_default_size(1920, 1080) #I set this to 1080p by default, simply change the values if you wish for the default screen to be smaller
        self.webview = webkit.WebView()
        self.webview.open(self.default_site)
        toolbar = gtk.Toolbar()
        #buttons
        self.back_button = gtk.ToolButton(gtk.STOCK_GO_BACK)
        self.back_button.connect("clicked", self.go_back)
        self.forward_button = gtk.ToolButton(gtk.STOCK_GO_FORWARD)
        self.forward_button.connect("clicked", self.go_forward)
        refresh_button = gtk.ToolButton(gtk.STOCK_REFRESH)
        refresh_button.connect("clicked", self.refresh)
        home_button = gtk.ToolButton(gtk.STOCK_HOME)
        home_button.connect("clicked",  self.go_home)
        #add buttons to toolbar
        toolbar.add(self.back_button)
        toolbar.add(self.forward_button)
        toolbar.add(refresh_button)
        toolbar.add(home_button)
        #search bar
        self.url_bar = gtk.Entry()
        self.url_bar.connect("activate", self.on_active)
        #call update button
        self.webview.connect("load_committed", self.update_buttons)
        self.window.set_title('Burrito - Browse The Web!' )
        self.window.set_icon_from_file('/home/pi/Burrito/icons/burrito.png')
        scroll_window = gtk.ScrolledWindow(None, None)
        scroll_window.add(self.webview)
        #window
        vbox = gtk.VBox(False, 0)
        vbox = gtk.VBox(spacing=5)
        vbox.set_border_width(1)
        vbox.pack_start(toolbar, False, True, 0)
        vbox.pack_start(self.url_bar, False, True, 0)
        vbox.add(scroll_window)
        self.window.add(vbox)
        self.window.show_all()
        print("Burrito has started...")
    def on_active(self, widge, data=None):
        url = self.url_bar.get_text()
        try:
            url.index("://")
        except:
            url = "http://"+url #add http:// if user didn't
        self.window.set_title('Burrito - Browse The Web - ' + url)
        self.url_bar.set_text(url)
        self.webview.open(url)
    def go_home(self, widget, data=None):
        self.webview.open(self.default_site)
    def go_back(self, widget, data=None):
        self.webview.go_back()
    def go_forward(self, widget, data=None):
        self.webview.go_forward()
    def refresh(self, widget, data=None):
        self.webview.reload()
    def update_buttons(self, widget, data=None):
        self.url_bar.set_text( widget.get_main_frame().get_uri() )
        self.back_button.set_sensitive(self.webview.can_go_back())
        self.forward_button.set_sensitive(self.webview.can_go_forward())
    def main(self):
        gtk.main()
if __name__ == "__main__":
    browser = Burrito()
    browser.main()
