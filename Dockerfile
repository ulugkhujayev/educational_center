FROM odoo:16.0

WORKDIR /odoo

COPY . /odoo

EXPOSE 8069

CMD ["odoo", "-i", "base"]