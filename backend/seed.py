from core.models import Sector
from tools.models import Tool
from tenants_management.models import Tenant

print("Seeding database...")

# ------------------------
# Sectors
# ------------------------

oil, _ = Sector.objects.get_or_create(name="Oil & Gas")
fisheries, _ = Sector.objects.get_or_create(name="Fisheries")
carbon, _ = Sector.objects.get_or_create(name="Carbon Market")
defense, _ = Sector.objects.get_or_create(name="Defense")
manufacturing, _ = Sector.objects.get_or_create(name="Manufacturing")

# ------------------------
# Tools
# ------------------------

predictive, _ = Tool.objects.get_or_create(
    name="AI Driven Predictive Maintenance Engine",
    defaults={
        "description": "Predict equipment failures before they occur",
        "category": "AI",
        "type": "Analytics",
        "status": "DEPLOYED",
    }
)

predictive.sectors.set([
    oil,
    manufacturing
])

analytics, _ = Tool.objects.get_or_create(
    name="Oil & Gas Analytics Engine",
    defaults={
        "description": "Production optimization and analytics",
        "category": "Analytics",
        "type": "Dashboard",
        "status": "DEPLOYED",
    }
)

analytics.sectors.set([oil])

carbon_tool, _ = Tool.objects.get_or_create(
    name="Carbon Credit Marketplace",
    defaults={
        "description": "Trade and manage carbon credits",
        "category": "Marketplace",
        "type": "Platform",
        "status": "DRAFT",
    }
)

carbon_tool.sectors.set([carbon])

marine_tool, _ = Tool.objects.get_or_create(
    name="Marine Resource Monitoring",
    defaults={
        "description": "Monitor marine ecosystems and resources",
        "category": "Monitoring",
        "type": "Analytics",
        "status": "DEPLOYED",
    }
)

marine_tool.sectors.set([fisheries])

defense_tool, _ = Tool.objects.get_or_create(
    name="Defense Surveillance Suite",
    defaults={
        "description": "Security and surveillance analytics",
        "category": "Security",
        "type": "Platform",
        "status": "DEPLOYED",
    }
)

defense_tool.sectors.set([defense])

# ------------------------
# Tenants
# ------------------------

naval, _ = Tenant.objects.get_or_create(
    name="Indian Naval Base",
    defaults={
        "tier": "PRO",
        "contact_name": "Naval Admin",
        "contact_email": "naval@gmail.com",
        "status": "ACTIVE",
    }
)

naval.sectors.set([
    defense,
    oil
])

naval.tools.set([
    predictive,
    analytics,
    defense_tool
])

bharat, _ = Tenant.objects.get_or_create(
    name="Bharat Petroleum",
    defaults={
        "tier": "ENTERPRISE",
        "contact_name": "Operations Head",
        "contact_email": "ops@bharatpetroleum.com",
        "status": "ACTIVE",
    }
)

bharat.sectors.set([
    oil,
    carbon
])

bharat.tools.set([
    predictive,
    analytics,
    carbon_tool
])

fishcorp, _ = Tenant.objects.get_or_create(
    name="FishCorp",
    defaults={
        "tier": "FREE",
        "contact_name": "Fish Manager",
        "contact_email": "manager@fishcorp.com",
        "status": "ACTIVE",
    }
)

fishcorp.sectors.set([
    fisheries
])

fishcorp.tools.set([
    marine_tool
])

print("Database seeded successfully!")