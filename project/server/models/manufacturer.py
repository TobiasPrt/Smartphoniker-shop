from project.server import db
from project.server.models.base import BaseModel
from project.server.models.image import ImageMixin


class Manufacturer(BaseModel, ImageMixin):
    __tablename__ = "manufacturer"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True, nullable=False)
    activated = db.Column(db.Boolean(), default=False)

    # Relations
    series = db.relationship("DeviceSeries", back_populates="manufacturer")

    def __repr__(self):
        return self.name

    @property
    def devices(self):
        return [devices for devices in self.series.devices]

    def _get_image_name_for_class(self):
        from project.server.models.image import Image, Default
        return Image.query.filter(Image.manufacturer_default == Default.true).first()  # noqa
