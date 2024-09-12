from jinja2 import Environment, FileSystemLoader
import pdfkit

# Set up Jinja2 environment
file_loader = FileSystemLoader('C:\\Users\\user\\Desktop\\invoice_generator')
template_env = Environment(loader=file_loader)

# Load the template
template = template_env.get_template('invoice.html')

# Data for template
data = {
    'invoice_number': '001',
    'invoice_date': '2024-09-10',
    'due_date': '2024-10-10',
    'seller_name': 'ABC Corp',
    'seller_address': '123 Business Rd',
    'seller_pan': 'ABCDE1234F',
    'seller_gst': '22ABCDE1234F1Z5',
    'billing_name': 'John Doe',
    'billing_address': '456 Residential St',
    'billing_state_code': 'XY',
    'shipping_name': 'John Doe',
    'shipping_address': '456 Residential St',
    'shipping_state_code': 'XY',
    'order_number': 'ORD123',
    'order_date': '2024-09-01',
    'place_of_supply': 'XYZ City',
    'place_of_delivery': 'XYZ City',
    'items': '''
    <tr>
        <td>Product 1</td>
        <td>$10.00</td>
        <td>2</td>
        <td>0</td>
        <td>$20.00</td>
        <td>5%</td>
        <td>GST</td>
        <td>$1.00</td>
        <td>$21.00</td>
    </tr>
    ''',
    'total_amount': '$21.00',
    'amount_in_words': 'Twenty-One Dollars',
    'signature_img': 'signature-placeholder.png'
}

# Render the template with data
html_content = template.render(data)

# Configure pdfkit
pdf_config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

# Generate PDF
pdfkit.from_string(html_content, 'invoice.pdf', configuration=pdf_config)
