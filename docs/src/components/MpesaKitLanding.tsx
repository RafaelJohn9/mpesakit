import React, { useEffect } from 'react';
import styles from './MpesaKit.module.css';
import { BackgroundAnimation } from './BackgroundAnimation';
import { HeroSection } from './HeroSection';
import { StatsSection } from './StatsSection';
import { FeaturesSection } from './FeaturesSection';
import { SecuritySection } from './SecuritySection';
import { APIStatusSection } from './APIStatusSection';
import { DocumentationSection } from './DocumentationSection';
import { CTASection } from './CTASection';
import { Footer } from './Footer';



export const MpesaKitLanding: React.FC = () => {
  useEffect(() => {
    // Intersection Observer for animations
    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add(styles.visible);
        }
      });
    }, observerOptions);

    // Observe all fade-in-up elements
    document.querySelectorAll(`.${styles.fadeInUp}`).forEach(el => {
      observer.observe(el);
    });

    // Create floating particles effect
    const createParticle = () => {
      const particle = document.createElement('div');
      particle.style.position = 'fixed';
      particle.style.width = '4px';
      particle.style.height = '4px';
      particle.style.background = 'var(--mpesa-green)';
      particle.style.borderRadius = '50%';
      particle.style.pointerEvents = 'none';
      particle.style.opacity = '0.6';
      particle.style.zIndex = '-1';

      const startX = Math.random() * window.innerWidth;
      const startY = window.innerHeight + 10;

      particle.style.left = startX + 'px';
      particle.style.top = startY + 'px';

      document.body.appendChild(particle);

      // Animate particle
      let y = startY;
      const speed = 0.5 + Math.random() * 1;

      const animateParticle = () => {
        y -= speed;
        particle.style.top = y + 'px';

        if (y < -10) {
          particle.remove();
        } else {
          requestAnimationFrame(animateParticle);
        }
      };

      animateParticle();
    };

    // Create particles occasionally
    const particleInterval = setInterval(createParticle, 3000);

    return () => {
      observer.disconnect();
      clearInterval(particleInterval);
    };
  }, []);

  // Data for components
  const heroData = {
    title: "MpesaKit",
    description: "Open-source Python M-Pesa SDK built by the community, for the community. A reliable third-party library that simplifies M-Pesa integration with comprehensive validation and developer-friendly design.",
    badges: ["Open Source", "99%+ Test Coverage", "300+ Test Cases", "Community Driven"],
    primaryCTA: {
      text: "🚀 Get Started",
      href: "https://mpesakit.readthedocs.io/en/latest/quickstart.html"
    },
    secondaryCTA: {
      text: "⭐ Star on GitHub",
      href: "https://github.com/rafaeljohn9/mpesakit"
    }
  };

  const statsData = [
    { number: "99%+", label: "Test Coverage" },
    { number: "300+", label: "Test Cases" },
    { number: "100%", label: "Type Hints" },
    { number: "24/7", label: "API Monitoring" }
  ];

  const featuresData = {
    title: "Why Choose MpesaKit?",
    subtitle: "Community-built features designed for real-world M-Pesa integration challenges",
    features: [
      {
        icon: "🔍",
        title: "Advanced Data Validation",
        description: "Comprehensive request and response schema validation ensures data integrity before hitting M-Pesa APIs.",
        features: [
          "Pydantic-powered schema validation",
          "Phone number format validation",
          "Amount range verification",
          "Callback URL security checks"
        ]
      },
      {
        icon: "🛡️",
        title: "Production Security",
        description: "Enterprise-grade security features to protect your transactions and sensitive data.",
        features: [
          "IP whitelist for callback endpoints",
          "SSL certificate validation",
          "Request signing & verification",
          "Token refresh automation"
        ]
      },
      {
        icon: "🎯",
        title: "Developer Experience",
        description: "Designed for developers who value clean code, type safety, and comprehensive documentation.",
        features: [
          "100% type hints coverage",
          "IntelliSense-friendly APIs",
          "Detailed error messages",
          "Rich debugging information"
        ]
      },
      {
        icon: "⚡",
        title: "High Customization",
        description: "Extensively configurable to meet any business requirement with flexible integration options.",
        features: [
          "Custom callback handlers",
          "Pluggable authentication",
          "Middleware support",
          "Flexible configuration"
        ]
      },
      {
        icon: "📊",
        title: "Complete API Coverage",
        description: "Full support for all M-Pesa Daraja APIs with real-time status monitoring.",
        features: [
          "STK Push (Lipa Na M-Pesa)",
          "C2B, B2C, B2B transactions",
          "Transaction status queries",
          "Account balance checks"
        ]
      },
      {
        icon: "🧪",
        title: "Battle-Tested Quality",
        description: "Extensive testing ensures reliability in production environments.",
        features: [
          "300+ comprehensive test cases",
          "99%+ code coverage",
          "Integration test suite",
          "Performance benchmarks"
        ]
      }
    ]
  };

  const securityData = {
    title: "Security & Reliability",
    description: "MpesaKit implements industry best practices to ensure your M-Pesa integrations are secure and reliable in production environments.",
    securityFeatures: [
      {
        icon: "🛡️",
        title: "IP Whitelisting",
        description: "Restrict callback URLs to trusted IP addresses"
      },
      {
        icon: "🔐",
        title: "SSL Validation",
        description: "Enforce HTTPS and validate certificates"
      },
      {
        icon: "🔑",
        title: "Token Management",
        description: "Secure token storage and automatic refresh"
      },
      {
        icon: "📝",
        title: "Request Signing",
        description: "Cryptographic signing of requests for authenticity"
      }
    ]
  };

  const statusData = {
    title: "API Status Monitor",
    subtitle: "Real-time status of M-Pesa Daraja APIs and MpesaKit services",
    statusItems: [
      {
        name: "Authorization",
        status: "working" as "working" | "down" | "maintenance",
        note: "OAuth token issuance and refresh endpoints operational",
        link: { text: "Authorization Docs", href: "https://mpesakit.readthedocs.io/en/latest/api.html#authorization" }
      },
      {
        name: "Dynamic QR",
        status: "working" as "working" | "down" | "maintenance",
        note: "QR generation and validation working as expected",
        link: { text: "Dynamic QR Docs", href: "https://mpesakit.readthedocs.io/en/latest/api.html#dynamic-qr" }
      },
      {
        name: "M-Pesa Express",
        status: "working" as "working" | "down" | "maintenance",
        note: "STK Push / Lipa Na M-Pesa flow operational",
        link: { text: "M-Pesa Express Docs", href: "https://mpesakit.readthedocs.io/en/latest/api.html#mpesa-express" }
      },
      {
        name: "Customer To Business (C2B)",
        status: "working" as "working" | "down" | "maintenance",
        note: "C2B payment endpoints accepting requests",
        link: { text: "C2B Docs", href: "https://mpesakit.readthedocs.io/en/latest/api.html#c2b" }
      },
      {
        name: "Business To Customer (B2C)",
        status: "working" as "working" | "down" | "maintenance",
        note: "B2C payouts processing normally",
        link: { text: "B2C Docs", href: "https://mpesakit.readthedocs.io/en/latest/api.html#b2c" }
      },
      {
        name: "Transaction Status",
        status: "working" as "working" | "down" | "maintenance",
        note: "Status queries returning timely responses",
        link: { text: "Transaction Status Docs", href: "https://mpesakit.readthedocs.io/en/latest/api.html#transaction-status" }
      },
      {
        name: "Account Balance",
        status: "working" as "working" | "down" | "maintenance",
        note: "Account balance checks operational",
        link: { text: "Account Balance Docs", href: "https://mpesakit.readthedocs.io/en/latest/api.html#account-balance" }
      },
      {
        name: "Reversals",
        status: "working" as "working" | "down" | "maintenance",
        note: "Reversal endpoints functional",
        link: { text: "Reversals Docs", href: "https://mpesakit.readthedocs.io/en/latest/api.html#reversals" }
      },
      {
        name: "Tax Remittance",
        status: "working" as "working" | "down" | "maintenance",
        note: "Tax remittance integration working",
        link: { text: "Tax Remittance Docs", href: "https://mpesakit.readthedocs.io/en/latest/api.html#tax-remittance" }
      },
      {
        name: "Business Pay Bill",
        status: "working" as "working" | "down" | "maintenance",
        note: "PayBill payment flows operational",
        link: { text: "Pay Bill Docs", href: "https://mpesakit.readthedocs.io/en/latest/api.html#pay-bill" }
      },
      {
        name: "Business Buy Goods",
        status: "working" as "working" | "down" | "maintenance",
        note: "BuyGoods payment flows operational",
        link: { text: "Buy Goods Docs", href: "https://mpesakit.readthedocs.io/en/latest/api.html#buy-goods" }
      },
      {
        name: "Bill Manager",
        status: "maintenance" as "working" | "down" | "maintenance",
        note: "On hold per Safaricom API support",
        link: { text: "Bill Manager (notes)", href: "https://mpesakit.readthedocs.io/en/latest/api.html#bill-manager" }
      },
      {
        name: "B2B Express Checkout",
        status: "maintenance" as "working" | "down" | "maintenance",
        note: "On hold per Safaricom API support",
        link: { text: "B2B Express (notes)", href: "https://mpesakit.readthedocs.io/en/latest/api.html#b2b-express" }
      },
      {
        name: "B2C Account Top Up",
        status: "working" as "working" | "down" | "maintenance",
        note: "Account top-up flows functioning normally",
        link: { text: "B2C Top Up Docs", href: "https://mpesakit.readthedocs.io/en/latest/api.html#b2c-top-up" }
      },
      {
        name: "M-Pesa Ratiba",
        status: "maintenance" as "working" | "down" | "maintenance",
        note: "On hold per Safaricom API support",
        link: { text: "Ratiba (notes)", href: "https://mpesakit.readthedocs.io/en/latest/api.html#ratiba" }
      }
    ]
  };

  const docsData = {
    title: "Comprehensive Documentation",
    subtitle: "Everything you need to get started and scale your M-Pesa integration",
    docItems: [
      {
        icon: "📚",
        title: "Quick Start Guide",
        description: "Get up and running in minutes with our step-by-step guide and code examples.",
        link: {
          text: "Start Building",
          href: "https://mpesakit.readthedocs.io/en/latest/quickstart.html"
        }
      },
      {
        icon: "🔧",
        title: "API Reference",
        description: "Complete API documentation with parameters, responses, and error codes.",
        link: {
          text: "View APIs",
          href: "https://mpesakit.readthedocs.io/en/latest/api.html"
        }
      },
      {
        icon: "💡",
        title: "Examples & Tutorials",
        description: "Real-world examples and tutorials for common integration patterns.",
        link: {
          text: "See Examples",
          href: "https://mpesakit.readthedocs.io/en/latest/examples.html"
        }
      }
    ]
  };

  const ctaData = {
    title: "Ready to Build?",
    description: "Join hundreds of developers who trust MpesaKit for their M-Pesa integrations. Start building secure, reliable payment solutions today.",
    primaryCTA: {
      text: "🚀 Get Started Now",
      href: "https://mpesakit.readthedocs.io/en/latest/quickstart.html"
    },
    secondaryCTA: {
      text: "📖 View Documentation",
      href: "https://github.com/rafaeljohn9/mpesakit"
    }
  };

  const footerData = {
    title: "MpesaKit",
    description: "Open-source Python M-Pesa SDK built by the community, for the community.",
    sections: [
      {
        title: "Resources",
        links: [
          { text: "Quick Start", href: "https://mpesakit.readthedocs.io/en/latest/quickstart.html" },
          { text: "API Reference", href: "https://mpesakit.readthedocs.io/en/latest/api.html" },
          { text: "Examples", href: "https://mpesakit.readthedocs.io/en/latest/examples.html" },
          { text: "Contributing", href: "https://mpesakit.readthedocs.io/en/latest/contributing.html" }
        ]
      },
      {
        title: "Community",
        links: [
          { text: "GitHub", href: "https://github.com/rafaeljohn9/mpesakit" },
          { text: "Issues", href: "https://github.com/rafaeljohn9/mpesakit/issues" },
          { text: "Discussions", href: "https://github.com/rafaeljohn9/mpesakit/discussions" },
          { text: "Discord", href: "https://discord.gg/vzGBh5Qu" },
          { text: "PyPI", href: "https://pypi.org/project/mpesakit/" }
        ]
      },
      {
        title: "Support",
        links: [
          { text: "FAQ", href: "https://mpesakit.readthedocs.io/en/latest/faq.html" },
          { text: "Report Bug", href: "https://github.com/rafaeljohn9/mpesakit/issues" },
          { text: "Get Help", href: "https://github.com/rafaeljohn9/mpesakit/discussions" },
          { text: "Changelog", href: "https://mpesakit.readthedocs.io/en/latest/changelog.html" }
        ]
      }
    ],
    socialLinks: [
      { text: "📱", href: "https://github.com/rafaeljohn9/mpesakit" },
      { text: "📦", href: "https://pypi.org/project/mpesakit/" },
      { text: "📚", href: "https://mpesakit.readthedocs.io" }
    ],
    copyright: "© 2025 MpesaKit. Open source project by John Kagunda",
    tagline: "Built with ❤️ for the community."
  };

  return (
    <div className={styles.mpesaKitLanding}>
      <BackgroundAnimation />
      <HeroSection {...heroData} />
      <StatsSection stats={statsData} />
      <FeaturesSection {...featuresData} />
      <SecuritySection {...securityData} />
      <APIStatusSection {...statusData} />
      <DocumentationSection {...docsData} />
      <CTASection {...ctaData} />
      <Footer {...footerData} />
    </div>
  );
};