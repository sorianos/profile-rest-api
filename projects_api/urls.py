from django.urls import path, include

from rest_framework.routers import DefaultRouter

from projects_api import views

router = DefaultRouter()
router.register('uses', views.UsesViewSet)
router.register('type-project', views.TypeProjectsViewSet)
router.register('countries', views.CountriesViewSet)
router.register('useful-life', views.UsefulLifeViewSet)
router.register('housing-scheme', views.HousingSchemeViewSet)
router.register('projects', views.ProjectsViewSet)
router.register('materials', views.MaterialsViewSet)
router.register('sections', views.SectionsViewSet)
router.register('origins', views.OriginsViewSet)
router.register('units', views.UnitsViewSet)
router.register('standards', views.StandardsViewSet)
router.register('potential-types', views.PotentialTypesViewSet)
router.register('volume-units', views.VolumeUnitsViewSet)
router.register('energy-units', views.EnergyUnitsViewSet)
router.register('bulk-units', views.BulkUnitsViewSet)
router.register('source-information', views.SourceInformationViewSet)
router.register('constructive-process', views.ConstructiveProcessViewSet)
router.register('material-scheme-project', views.MaterialSchemeProjectViewSet)
router.register('material-scheme-data', views.MaterialSchemeDataViewSet)
router.register('constructive-system-element', views.ConstructiveSystemElementViewSet)
router.register('sources-electricity-consumption', views.SourcesElectricityConsumptionViewSet)
router.register('annual-consumption-required', views.AnnualConsumptionRequiredViewSet)
router.register('electricity-consumption-data', views.ElectricityConsumptionDataViewSet)
router.register('stage-scheme-data', views.StageSchemeDataViewSet)
router.register('type-energy', views.TypeEnergyViewSet)
router.register('electricity-consumption-deconstructive-process', views.ElectricityConsumptionDeconstructiveProcessViewSet)
router.register('treatment-of-generate-wasted', views.TreatmentOfGeneratedWasteViewSet)

urlpatterns = [
    path('', include(router.urls))
]
