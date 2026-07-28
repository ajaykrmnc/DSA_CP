public class Product {
    private final String code;
    private final String name;
    private final Money price;
    private final ProductCategory category;

    public Product(String code, String name, Money price, ProductCategory category) {
        this.code = code;
        this.name = name;
        this.price = price;
        this.category = category;
    }
}

public class Inventory {
    private final Map<String, ProductSlot> slots;
    private final List<InventoryObserver> observers;

    public Inventory(int numSlots) {
        this.slots = new LinkedHashMap<>();
        this.observers = new ArrayList<>();
    }

    public boolean isAvailable(String code) {
        ProductSlot slot = slots.get(code);
        return slot != null && slot.getQuantity() > 0;
    }

    public Product dispense(String code) {
        ProductSlot slot = slots.get(code);
        if (slot == null || slot.getQuantity() <= 0) {
            throw new OutOfStockException(code);
        }

        slot.decrementQuantity();

        if (slot.getQuantity() <= slot.getLowStockThreshold()) {
            notifyLowStock(slot);
        }

        return slot.getProduct();
    }

    public void restock(String code, int quantity) {
        ProductSlot slot = slots.get(code);
        if (slot != null) {
            slot.addQuantity(quantity);
        }
    }

    public List<ProductInfo> getAvailableProducts() {
        return slots.values().stream()
            .filter(slot -> slot.getQuantity() > 0)
            .map(slot -> new ProductInfo(
                slot.getProduct().getCode(),
                slot.getProduct().getName(),
                slot.getProduct().getPrice(),
                slot.getQuantity()
            ))
            .collect(Collectors.toList());
    }
}

class ProductSlot {
    private final Product product;
    private int quantity;
    private final int maxCapacity;
    private final int lowStockThreshold;
}
