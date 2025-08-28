// components/StatsSection.tsx
import styles from './MpesaKit.module.css';

interface StatItem {
  number: string;
  label: string;
}

interface StatsSectionProps {
  stats: StatItem[];
}

export const StatsSection: React.FC<StatsSectionProps> = ({ stats }) => {
  return (
    <section className={`${styles.stats} ${styles.fadeInUp}`}>
      <div className={styles.statsContainer}>
        {stats.map((stat, index) => (
          <div key={index} className={styles.statCard}>
            <div className={styles.statNumber}>{stat.number}</div>
            <div className={styles.statLabel}>{stat.label}</div>
          </div>
        ))}
      </div>
    </section>
  );
};