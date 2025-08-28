// components/APIStatusSection.tsx
import styles from './MpesaKit.module.css';

interface StatusItem {
  name: string;
  status: 'working' | 'maintenance' | 'down';
  note: string;
  link?: {
    text: string;
    href: string;
  };
}

interface APIStatusSectionProps {
  title: string;
  subtitle: string;
  statusItems: StatusItem[];
}

export const APIStatusSection: React.FC<APIStatusSectionProps> = ({
  title,
  subtitle,
  statusItems
}) => {
  return (
    <section className={`${styles.apiStatus} ${styles.fadeInUp}`} id="status">
      <div className={styles.featuresContainer}>
        <div className={styles.sectionTitle}>
          <h2>{title}</h2>
          <p>{subtitle}</p>
        </div>

        <div className={styles.statusGrid}>
          {statusItems.map((item, index) => (
            <StatusCard key={index} {...item} />
          ))}
        </div>
      </div>
    </section>
  );
};

const StatusCard: React.FC<StatusItem> = ({
  name,
  status,
  note,
  link,
}) => {
  return (
    <div className={styles.statusCard}>
      <div className={styles.statusHeader}>
        <h3>{name}</h3>
        <div className={`${styles.statusIndicator} ${styles[`status${status.charAt(0).toUpperCase() + status.slice(1)}`]}`}></div>
      </div>
      <div className={styles.statusDetails}>
        <span>{note}</span>
      </div>
      {link && (
        <div className={styles.statusFooter}>
          <a
            href={link.href}
            target="_blank"
            rel="noopener noreferrer"
            className={styles.statusLink}
          >
            {link.text}
          </a>
        </div>
      )}
    </div>
  );
};
