from exts import db
from marshmallow import fields, Schema


class EnterpriseInfo(db.Model):
    __tablename__ = 'enterprise_info'

    id = db.Column(db.Integer, primary_key=True)
    firm_eid = db.Column(db.String(36))
    firm_name = db.Column(db.String)
    usc_code = db.Column(db.String)
    firm_category = db.Column(db.String)
    ope_status = db.Column(db.Text)
    legal_rep = db.Column(db.String)
    legal_rep_type = db.Column(db.Text)
    legal_rep_category = db.Column(db.String)
    firm_type = db.Column(db.String)
    firm_org_type = db.Column(db.String)
    est_date = db.Column(db.String)
    cancel_date = db.Column(db.String)
    rev_certificates = db.Column(db.String)
    reg_agency = db.Column(db.String)
    reg_agency_area_code = db.Column(db.String)
    usc_code_area_code = db.Column(db.String)
    appr_date = db.Column(db.String)
    open_date = db.Column(db.String)
    close_date = db.Column(db.String)
    province = db.Column(db.String)
    city = db.Column(db.Text)
    district = db.Column(db.String)
    bd_longitude = db.Column(db.Text)
    bd_latitude = db.Column(db.Text)
    gd_longitude = db.Column(db.Text)
    gd_latitude = db.Column(db.Text)
    reg_cap = db.Column(db.String)
    reg_cap_cur = db.Column(db.Text)
    ope_scope = db.Column(db.Text)
    first_year_judicial_count = db.Column(db.BigInteger)
    second_year_judicial_count = db.Column(db.BigInteger)
    third_year_judicial_count = db.Column(db.BigInteger)
    first_year_registraion_count = db.Column(db.BigInteger)
    second_year_registraion_count = db.Column(db.BigInteger)
    third_year_registraion_count = db.Column(db.BigInteger)
    first_year_involve_amt = db.Column(db.BigInteger)
    second_year_involve_amt = db.Column(db.BigInteger)
    third_year_involve_amt = db.Column(db.BigInteger)
    first_year_executor_count = db.Column(db.BigInteger)
    second_year_executor_count = db.Column(db.BigInteger)
    third_year_executor_count = db.Column(db.BigInteger)

    def __repr__(self):
        return f"firm_name={self.firm_name}"

    def __str__(self):
        return f"firm_name={self.firm_name}"


class EnterpriseInfoSchema(Schema):
    id = fields.Integer()
    firm_eid = fields.String()
    firm_name = fields.String()
    usc_code = fields.String()
    firm_category = fields.String()
    ope_status = fields.String()
    legal_rep = fields.String()
    legal_rep_type = fields.String()
    legal_rep_category = fields.String()
    firm_type = fields.String()
    firm_org_type = fields.String()
    est_date = fields.String()
    cancel_date = fields.String()
    rev_certificates = fields.String()
    reg_agency = fields.String()
    reg_agency_area_code = fields.String()
    usc_code_area_code = fields.String()
    appr_date = fields.String()
    open_date = fields.String()
    close_date = fields.String()
    province = fields.String()
    city = fields.String()
    district = fields.String()
    bd_longitude = fields.String()
    bd_latitude = fields.String()
    gd_longitude = fields.String()
    gd_latitude = fields.String()
    reg_cap = fields.String()
    reg_cap_cur = fields.String()
    ope_scope = fields.String()
    first_year_judicial_count = fields.Integer()
    second_year_judicial_count = fields.Integer()
    third_year_judicial_count = fields.Integer()
    first_year_registraion_count = fields.Integer()
    second_year_registraion_count = fields.Integer()
    third_year_registraion_count = fields.Integer()
    first_year_involve_amt = fields.Integer()
    second_year_involve_amt = fields.Integer()
    third_year_involve_amt = fields.Integer()
    first_year_executor_count = fields.Integer()
    second_year_executor_count = fields.Integer()
    third_year_executor_count = fields.Integer()

