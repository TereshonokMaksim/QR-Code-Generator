from django.contrib import admin
from django.utils.html import format_html
from .models import QRCode

# Register your models here.

class QRCodeImageAdmin(admin.ModelAdmin):
    def image_tag(self, qrcode):
        return format_html(f"""
                <div class = "fullImageBlur" style = "display: none;  position: absolute;  flex-direction: column;  align-items: center;  justify-content: center;  gap: 30px;  width: 100%;  height: 100vh;  left: 0px;  top: 0px;  background-color: rgba(0, 0, 0, 0.5);  z-index: 21">
                    <img src = '{qrcode.path_qrcode.url}' style='border-radius:20px;  height: 90%;' class = 'fullImage'/>
                    <button style="padding:5px 10px; background:#007bff; color:white; border:none; border-radius:5px; cursor:pointer; font-size: 32px" onclick='document.querySelector(".fullImageBlur").style.display = "none"; document.body.style.overflowY = "scroll"' type = "button">Close</button>
                </div>
                <button style="padding:5px 10px; background:#007bff; color:white; border:none; border-radius:5px; cursor:pointer;" onclick='let blur = document.querySelector(".fullImageBlur"); blur.style.display = "flex"; blur.style.top = String(window.scrollY) + "px"; document.body.style.overflowY = "hidden"; ' type = "button">View Full Image</button>
                <br><br>
                <img src='{qrcode.path_qrcode.url}' width='300' style='border-radius:10px'/>""")
    def front_color(self, qrcode):
        return format_html(f"""
                <div style = "display: flex;  flex-direction: row; align-items: center;  gap: 10px;">
                    <div style = "border-radius: 10px;  border: 1px solid black;  width: 50px;  height: 15px;  background-color: #{qrcode.color_front}">
                    </div>
                    <p>#{qrcode.color_front}</p>
                </div>
            """)
    def back_color(self, qrcode):
        return format_html(f"""
                <div style = "display: flex;  flex-direction: row; align-items: center;  gap: 10px;">
                    <div style = "border-radius: 10px;  border: 1px solid black;  width: 50px;  height: 15px;  background-color: #{qrcode.color_back}">
                    </div>
                    <p>#{qrcode.color_back}</p>
                </div>
            """)
    image_tag.short_description = "Ready QR Code"
    front_color.short_description = "Front color"
    back_color.short_description = "Back color"
    readonly_fields = ('image_tag', 'front_color', 'back_color')
    fields = ['name','image_tag', 'front_color', 'back_color', 'form', 'link', 'acc_id', 'when_created']

admin.site.register(QRCode, QRCodeImageAdmin)