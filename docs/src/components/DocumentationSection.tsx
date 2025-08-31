// components/DocumentationSection.tsx
import styles from './MpesaKit.module.css';


interface DocItem {
  icon: string;
  title: string;
  description: string;
  link: {
    text: string;
    href: string;
  };
}

interface DocumentationSectionProps {
  title: string;
  subtitle: string;
  docItems: DocItem[];
}

export const DocumentationSection: React.FC<DocumentationSectionProps> = ({
  title,
  subtitle,
  docItems
}) => {
  return (
    <section className={`${styles.documentation} ${styles.fadeInUp}`}>
      <div className={styles.docContainer}>
        <div className={styles.sectionTitle}>
          <h2>{title}</h2>
          <p>{subtitle}</p>
        </div>

        <div className={styles.docGrid}>
          {docItems.map((item, index) => (
            <div key={index} className={styles.docCard}>
              <div className={styles.docIcon}>{item.icon}</div>
              <h3>{item.title}</h3>
              <p>{item.description}</p>
              <a href={item.link.href} className={`${styles.btn} ${styles.btnSecondary}`} style={{ marginTop: '1rem' }}>
                {item.link.text}
              </a>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};