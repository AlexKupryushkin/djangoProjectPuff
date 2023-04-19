      const itemsCounter = document.querySelector(".items-total-count");
      const addItemBtn = document.querySelector(".add-item-btn");
      const removeItemBtn = document.querySelector(".remove-item-btn");
      const addToBagBtn = document.querySelector(".add-to-bag-btn");

      addItemBtn.addEventListener("click", increaseItemsCounter);
      removeItemBtn.addEventListener("click", decreaseItemsCounter);

      function increaseItemsCounter() {
        let itemsCounerCurrentValue = itemsCounter.innerHTML;
        if (Number(itemsCounerCurrentValue) === 0) {
            addToBagBtn.removeAttribute("disabled");
        }
        const updatedCount = ++itemsCounerCurrentValue;
        itemsCounter.innerHTML = updatedCount;
      }

    function decreaseItemsCounter() {
        let itemsCounerCurrentValue = itemsCounter.innerHTML;
        if (Number(itemsCounerCurrentValue) === 1) {
            addToBagBtn.setAttribute("disabled", "");
            const updatedCount = --itemsCounerCurrentValue;
            itemsCounter.innerHTML = updatedCount;
        } else if (Number(itemsCounerCurrentValue) > 1) {
            const updatedCount = --itemsCounerCurrentValue;
            itemsCounter.innerHTML = updatedCount;

        }
      }