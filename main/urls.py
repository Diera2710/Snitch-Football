from django.urls import path
from main.views import (
    show_main, create_product, show_product,
    show_xml, show_json, show_xml_by_id, show_json_by_id,
    register, login_user, logout_user, proxy_image,
    edit_product, delete_product,
    update_product_entry_ajax, delete_product_entry_ajax,
    add_product_entry_ajax,
    create_product_flutter,  
    show_json_user
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),

    # === XML / JSON (JANGAN TARUH DI BAWAH!) ===
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:product_id>/', show_json_by_id, name='show_json_by_id'),

    # Tambahan baru!!!
    path('product/json/', show_json, name='show_json_product'),
    path('create-product-flutter/', create_product_flutter, name='create_product_flutter'),



    # === AUTH ===
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    # === AJAX ===
    path('create-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('product/<int:id>/update-ajax', update_product_entry_ajax, name='update_product_entry_ajax'),
    path('product/<int:id>/delete-ajax', delete_product_entry_ajax, name='delete_product_entry_ajax'),

    # === PRODUCT DETAIL / EDIT / DELETE (harus terakhir!) ===
    path('product/<int:id>/', show_product, name='show_product'),
    path('product/<int:id>/edit', edit_product, name='edit_product'),
    path('product/<int:id>/delete', delete_product, name='delete_product'),
    path('product/json/user/', show_json_user, name='show_json_user'),


    # === PROXY IMAGE ===
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('create-product-flutter/', create_product_flutter, name='create_product_flutter'),


    

]
