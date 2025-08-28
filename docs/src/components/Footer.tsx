import styles from './MpesaKit.module.css';

interface FooterLink {
  text: string;
  href: string;
}

interface FooterSection {
  title: string;
  links: FooterLink[];
}

interface FooterProps {
  title: string;
  description: string;
  sections: FooterSection[];
  socialLinks: FooterLink[];
  copyright: string;
  tagline: string;
}

export const Footer: React.FC<FooterProps> = ({
  title,
  description,
  sections,
  socialLinks,
  copyright,
  tagline
}) => {
  return (
    <footer className={styles.footer}>
      <div className={styles.footerContainer}>
        <div className={styles.footerSection}>
          <h3>{title}</h3>
          <p style={{ color: 'var(--text-secondary)', marginBottom: '1rem' }}>
            {description}
          </p>
          <div className={styles.socialLinks}>
            {socialLinks.map((link, index) => (
              <a key={index} href={link.href}>
                {link.text}
              </a>
            ))}
          </div>
        </div>

        {sections.map((section, index) => (
          <div key={index} className={styles.footerSection}>
            <h3>{section.title}</h3>
            <ul>
              {section.links.map((link, linkIndex) => (
                <li key={linkIndex}>
                  <a href={link.href}>{link.text}</a>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>

      <div className={styles.footerBottom}>
        <p>{copyright}</p>
        <p style={{ marginTop: '0.5rem', fontSize: '0.9rem' }}>{tagline}</p>
      </div>
    </footer>
  );
};
