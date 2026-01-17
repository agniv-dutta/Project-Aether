"""Generate a messy, unorganized test PDF with tables (realistic real-world document)."""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def create_messy_pdf_with_tables(filename="messy_report_with_tables.pdf"):
    """Create a realistic, messy business report PDF with tables."""
    
    doc = SimpleDocTemplate(filename, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    
    # Title
    story.append(Paragraph("<b>QUARTERLY PERFORMANCE ANALYSIS - Q4 2025</b>", styles['Title']))
    story.append(Paragraph("Internal Document | Confidential | Last Updated: Jan 14, 2026", styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    
    # Executive Summary
    story.append(Paragraph("<b>Executive Summary (DRAFT - NOT FINAL)</b>", styles['Heading2']))
    story.append(Paragraph(
        "Q4 saw significant market challenges, particularly in EMEA region. Revenue growth "
        "was 6.2% YoY but only 2.1% QoQ. This is concerning given market conditions. We need "
        "to review strategy ASAP. The new commission structure, implemented in October, has shown "
        "positive initial results by increasing sales velocity by 14%, despite a 9% rise in "
        "Customer churn slightly increased to 12% from 10.5% in Q3.",
        styles['Normal']
    ))
    story.append(Spacer(1, 0.2*inch))
    
    # Table 1: Regional Revenue Breakdown
    story.append(Paragraph("<b>Regional Revenue Performance</b>", styles['Heading3']))
    regional_data = [
        ['Region', 'Q4 2025', 'Q3 2025', 'YoY Growth', 'Target', 'Status'],
        ['North America', '$2.3M', '$2.0M', '+15%', '$2.4M', '✓ Near Target'],
        ['Europe (EMEA)', '$1.8M', '$1.96M', '-8%', '$2.2M', '✗ URGENT'],
        ['APAC', '$1.1M', '$0.95M', '+16%', '$1.2M', '✓ On Track'],
        ['TOTAL', '$5.2M', '$4.91M', '+6%', '$5.8M', '✗ Below Target'],
    ]
    
    regional_table = Table(regional_data, colWidths=[1.5*inch, 1*inch, 1*inch, 1*inch, 1*inch, 1.2*inch])
    regional_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -2), colors.beige),
        ('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ]))
    story.append(regional_table)
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph(
        "<b>NOTE:</b> Spanish office data missing - still waiting on Maria's report. "
        "EMEA figures may increase by ~$200K once complete.",
        styles['Normal']
    ))
    story.append(Spacer(1, 0.3*inch))
    
    # Table 2: Sales Team Performance
    story.append(Paragraph("<b>Sales Team Performance by Vertical</b>", styles['Heading3']))
    sales_team_data = [
        ['Vertical', 'Team Size', 'Deals Closed', 'Avg Deal Size', 'Revenue', 'Pipeline'],
        ['Enterprise', '5 reps, 3 SDRs', '12', '$180K', '$2.16M', '$4.2M'],
        ['SMB', '8 reps, 5 SDRs', '45', '$65K', '$2.93M', '$2.8M'],
        ['Startup (NEW)', '4 reps, 2 SDRs', '30', '$28K', '$0.84M', '$1.5M'],
        ['TOTAL', '24 FTE', '87', '$59.7K avg', '$5.93M', '$8.5M'],
    ]
    
    sales_table = Table(sales_team_data, colWidths=[1.2*inch, 1.3*inch, 1*inch, 1*inch, 1*inch, 1*inch])
    sales_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3b82f6')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -2), colors.beige),
        ('BACKGROUND', (0, -1), (-1, -1), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    story.append(sales_table)
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph(
        "<b>Issues:</b> Mike (Enterprise) underperforming - PIP discussion pending. "
        "SMB performance uneven - some reps at $800K/year, others at $400K. "
        "Startup vertical sustainable long-term?",
        styles['Normal']
    ))
    story.append(Spacer(1, 0.3*inch))
    
    # Table 3: Customer Metrics
    story.append(PageBreak())
    story.append(Paragraph("<b>Customer Health Metrics</b>", styles['Heading3']))
    customer_data = [
        ['Metric', 'Q4 2025', 'Q3 2025', 'Q2 2025', 'Trend'],
        ['Total Customers', '312', '295', '271', '↑ Growing'],
        ['New Acquisitions', '87', '112', '94', '↓ Declining'],
        ['Churn Count', '37', '31', '28', '↑ CONCERN'],
        ['Churn Rate', '12.0%', '10.5%', '10.3%', '↑ CONCERN'],
        ['Net New Customers', '50', '81', '66', '↓ Declining'],
        ['Avg Customer LTV', '$289K', '$276K', '$265K', '↑ Positive'],
    ]
    
    customer_table = Table(customer_data, colWidths=[1.8*inch, 1.2*inch, 1.2*inch, 1.2*inch, 1.2*inch])
    customer_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#10b981')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgoldenrodyellow),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))
    story.append(customer_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Table 4: Competition Analysis
    story.append(Paragraph("<b>Competitive Landscape</b>", styles['Heading3']))
    competition_data = [
        ['Competitor', 'Market Entry', 'Pricing', 'Target', 'Threat Level'],
        ['TechStart Solutions', 'Oct 2025', 'Aggressive (-30%)', 'SMB/Startup', 'HIGH ⚠'],
        ['CloudPro Analytics', 'Nov 2025', 'Premium (+15%)', 'Enterprise', 'MEDIUM'],
        ['DataFlow Systems', 'Dec 2025', 'Budget (-20%)', 'Startup', 'MEDIUM'],
        ['Incumbent Inc.', 'Pre-2023', 'Standard', 'All', 'LOW'],
    ]
    
    comp_table = Table(competition_data, colWidths=[1.5*inch, 1.2*inch, 1.3*inch, 1.2*inch, 1.3*inch])
    comp_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#ef4444')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lavenderblush),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    story.append(comp_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Messy notes section
    story.append(Paragraph("<b>POLICY & ORGANIZATIONAL CHANGES</b>", styles['Heading2']))
    story.append(Paragraph(
        "New commission structure effective Oct 1: Increased base from $55K to $60K. "
        "Commission rate: 8% (was 6%). Accelerators for 150%+ of quota. Clawback clause "
        "if customer churns within 12mo. Impact: Payroll increased ~9%, but sales velocity "
        "up 14%. Is this sustainable long-term? CFO concerned about margins.",
        styles['Normal']
    ))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph(
        "New CRM system (Salesforce) rollout in Nov - 2 weeks late due to migration issues. "
        "Data quality issues persist. ~15% of opportunities lack clear close dates. "
        "Training: Minimal (1 hr session) - many reps not using it correctly yet.",
        styles['Normal']
    ))
    story.append(Spacer(1, 0.3*inch))
    
    # Action items
    story.append(Paragraph("<b>ACTION ITEMS / TODO:</b>", styles['Heading3']))
    actions = [
        "[ ] Review EMEA strategy - assign owner (Robert?)",
        "[ ] Root cause analysis on churn - Hannah (customer success)",
        "[ ] Update sales enablement deck",
        "[ ] CRM training session #2 (Jan 20)",
        "[ ] Evaluate pricing strategy vs competitors",
        "[ ] PIP discussion with Mike - HR involved",
        "[ ] Financial impact analysis of new comp structure",
    ]
    for action in actions:
        story.append(Paragraph(action, styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    
    # Assumptions and limitations
    story.append(Paragraph("<b>ASSUMPTIONS:</b>", styles['Heading3']))
    story.append(Paragraph(
        "Market growth continues at 20% YoY. No major economic downturn in 2026. "
        "2 competitors will be acquired/fail by end of 2026. New team members reach "
        "70% productivity by April. Churn stabilizes to 10% by Q2. EMEA recovers with strategic focus.",
        styles['Normal']
    ))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>LIMITATIONS OF THIS REPORT:</b>", styles['Heading3']))
    story.append(Paragraph(
        "EMEA data 2 weeks delayed (missing Spain/Portugal data). CRM data incomplete due to "
        "migration issues. Comp analysis based on Q4 only (seasonal?). Customer feedback limited "
        "to 12 surveyed (vs 300+ customers). Pipeline figures unverified by finance. "
        "Some data pulled manually (error risk).",
        styles['Normal']
    ))
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph(
        "<b>Next review:</b> Feb 15, 2026<br/>"
        "<b>Prepared by:</b> Sales Analytics Team<br/>"
        "<b>Reviewed by:</b> VP Sales, Finance Director (pending)",
        styles['Normal']
    ))
    
    # Build PDF
    doc.build(story)
    print(f"✅ Messy realistic PDF with tables created: {filename}")

if __name__ == "__main__":
    create_messy_pdf_with_tables()
