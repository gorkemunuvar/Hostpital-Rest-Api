import base64
import cx_Oracle


class ImageHandler():
    @staticmethod
    def convert_lob_to_base64_str(blob_image: cx_Oracle.LOB) -> str:
        image_bytes = blob_image.read()
        image_base64 = base64.b64encode(image_bytes)
        image_base64_str = image_base64.decode('utf-8')

        return image_base64_str
