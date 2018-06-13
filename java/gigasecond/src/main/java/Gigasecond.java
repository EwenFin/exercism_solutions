import java.sql.Timestamp;
import java.time.LocalDate;
import java.time.LocalDateTime;

public class Gigasecond {
    private final long gigaSecond = (long) Math.pow(10, 9);
    private LocalDateTime localDateTime;

    public Gigasecond(LocalDateTime localDateTime) {
        this.localDateTime = localDateTime;
    }

    public Gigasecond(LocalDate localDate) {
        this.localDateTime = localDate.atStartOfDay();
    }

    public LocalDateTime getDate() {
        return localDateTime.plusSeconds(gigaSecond);
    }
}