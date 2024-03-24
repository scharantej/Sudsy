**Flask Application Design for a Simple Soap Store Landing Page**

**HTML Files**

* **index.html**:
    * Main landing page of the website, featuring images of soap products, product descriptions, and call-to-actions.

* **about.html**:
    * Provides information about the store, its mission, and its team.

* **contact.html**:
    * Allows users to contact the store via a form, including contact details and address.

**Routes**

* **/**: Routes to the index.html page.
* **/about**: Routes to the about.html page.
* **/contact**: Routes to the contact.html page.
* **/soap/<soap_id>**: Routes to a specific soap product page, displaying product details, images, and add-to-cart functionality.
* **/cart**: Displays the current user's shopping cart and allows them to checkout or add more items.
* **/checkout**: Processes the user's order and handles payment.